from model.contact import Contact
import random


def test_update_contact_lastname(app, db, check_ui):
    if len(db.get_contacts()) == 0:
        app.contact.add(Contact(firstname='Anne', lastname='Murphy'))
    old_contacts = db.get_contacts()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_data = (Contact(lastname='Lewis'))
    new_data.id = contact.id
    new_data.firstname = contact.firstname
    app.contact.update_by_id(contact.id, new_data)
    new_contacts = db.get_contacts()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = new_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts(), key=Contact.id_or_max)
