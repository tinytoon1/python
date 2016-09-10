import pytest
import json
import os.path
import jsonpickle
from fixture.application import Application
from fixture.db import DBFixture
from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config:
            target = json.load(config)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid:
        fixture = Application(baseurl=web_config["baseURL"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    db_fixture = DBFixture(host=db_config["host"], database=db_config["name"], user=db_config["user"], password=db_config["password"])

    def fin():
        db_fixture.destroy()
    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture(scope="session")
def orm(request):
    orm_config = load_config(request.config.getoption("--target"))["db"]
    orm_fixture = ORMFixture(host=orm_config["host"], database=orm_config["name"], user=orm_config["user"], password=orm_config["password"])
    return orm_fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as data:
        return jsonpickle.decode(data.read())
