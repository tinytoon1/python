# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='first contact'))
    app.contact.delete()
