from model.contact import Contact
import random
import pytest


def test_update_contact_lastname(app, orm):
    with pytest.allure.step('Given non-empty contacts'):
        if len(orm.get_contacts()) == 0:
            app.contact.add(Contact(firstname='Anne', lastname='Murphy'))
        old_contacts = orm.get_contacts()
    with pytest.allure.step('When update firstname for contact'):
        contact = random.choice(old_contacts)
        index = old_contacts.index(contact)
        new_data = (Contact(lastname='Lewis'))
        new_data.id = contact.id
        new_data.firstname = contact.firstname
        app.contact.update_by_id(contact.id, new_data)
    with pytest.allure.step('Then the new contacts are equal to the old contacts after updating'):
        new_contacts = orm.get_contacts()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[index] = new_data
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
