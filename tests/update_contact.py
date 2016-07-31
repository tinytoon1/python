# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_update_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='Anne', lastname='Murphy'))
    old_contacts = app.contact.get_contacts()
    index = randrange(len(old_contacts))
    contact = (Contact(lastname='Lewis'))
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.update(index, contact)
    new_contacts = app.contact.get_contacts()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
