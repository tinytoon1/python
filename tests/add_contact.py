# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Alex", lastname="Murphy", company="OCP", address="Detroit", mobile="88005555555"))
    app.session.logout()
