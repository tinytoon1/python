import json
import os.path
from fixture.application import Application
from fixture.db import DBFixture
from model.contact import Contact


class addressbook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json"):
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as config:
            self.target = json.load(config)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(baseurl=web_config["baseURL"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target["db"]
        self.db_fixture = DBFixture(host=db_config["host"], database=db_config["name"], user=db_config["user"],
                               password=db_config["password"])

    def get_contacts(self):
        return self.db_fixture.get_contacts()

    def new_contact(self, firstname, lastname):
        return Contact(firstname=firstname, lastname=lastname)

    def contacts_should_be_equal(self, old_contacts, new_contacts):
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def add(self, contact):
        self.fixture.contact.add(contact)

    def delete(self, contact):
        self.fixture.contact.delete_by_id(contact.id)

    def update(self, contact, data):
        self.fixture.contact.update_by_id(contact.id, data)

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.db_fixture.destroy()
