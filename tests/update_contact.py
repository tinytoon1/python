# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update(Contact(firstname='empty contact'))
    app.session.logout()
