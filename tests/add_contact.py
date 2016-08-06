# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts()
    contact = Contact(firstname="Alex", lastname="Murphy", address="Detroit", homephone="222",
                      mobilephone="8(800)5555555", workphone="77-7", email="mail", email2="mail2", email3="mail3")
    app.contact.add(contact)
    new_contacts = app.contact.get_contacts()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
