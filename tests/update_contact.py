# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='first contact'))
    app.contact.update(Contact(mobile='88009999999'))
