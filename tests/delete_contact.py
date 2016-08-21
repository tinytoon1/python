from model.contact import Contact
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contacts()) == 0:
        app.contact.add(Contact(firstname='first contact'))
    old_contacts = db.get_contacts()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contacts()
    #assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    #assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts(), key=Contact.id_or_max)
