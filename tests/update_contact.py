# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='Anne', lastname='Lewis'))
    old_contacts = app.contact.get_contacts()
    contact = (Contact(lastname='Murphy'))
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    app.contact.update(contact)
    new_contacts = app.contact.get_contacts()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
