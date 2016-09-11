from model.contact import Contact
import pytest


def test_add_contact(app, orm, json_contacts):
    contact = json_contacts
    with pytest.allure.step('Given contacts'):
        old_contacts = orm.get_contacts()
    with pytest.allure.step('When add a new contact %s' % contact):
        app.contact.add(contact)
    with pytest.allure.step('Then the new contacts are equal to the old one'):
        new_contacts = orm.get_contacts()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
