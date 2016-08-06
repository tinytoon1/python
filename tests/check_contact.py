# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_check_contact_info(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='Alex', lastname='Murphy'))
    contacts = app.contact.get_contacts()
    index = randrange(len(contacts))
    homepage_info = contacts[index]
    edit_page_info = app.contact.get_info_from_edit_page(index)
    assert homepage_info.firstname == edit_page_info.firstname
    assert homepage_info.lastname == edit_page_info.lastname
    assert homepage_info.address == edit_page_info.address
    assert homepage_info.phones == app.contact.merge_phones(edit_page_info)
    assert homepage_info.emails == app.contact.merge_emails(edit_page_info)
