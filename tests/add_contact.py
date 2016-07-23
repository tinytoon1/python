# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="Alex", lastname="Murphy", company="OCP", address="Detroit", mobile="88005555555"))
    app.session.logout()
