# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add(Contact(firstname="Alex", lastname="Murphy", company="OCP", address="Detroit", mobile="88005555555"))
