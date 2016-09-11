from model.contact import Contact
import random
import pytest


def test_delete_contact(app, orm):
    with pytest.allure.step('Given non-empty contacts'):
        if len(orm.get_contacts()) == 0:
            app.contact.add(Contact(firstname='first contact'))
        old_contacts = orm.get_contacts()
    with pytest.allure.step('When delete contact'):
        contact = random.choice(old_contacts)
        app.contact.delete_by_id(contact.id)
    with pytest.allure.step('the new contacts are equal to the old contacts without the deleted contact'):
        new_contacts = orm.get_contacts()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
