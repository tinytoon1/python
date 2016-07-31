# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='first contact'))
    old_contacts = app.contact.get_contacts()
    app.contact.delete()
    new_contacts = app.contact.get_contacts()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
