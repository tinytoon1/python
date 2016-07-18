# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first(Contact(firstname='empty contact', lastname='', company='', address='', mobile=''))
    app.session.logout()
