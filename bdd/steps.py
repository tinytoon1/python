from pytest_bdd import given, when, then
from model.contact import Contact
from random import choice


@given('contacts')
def contacts(db):
    return db.get_contacts()


@given('new contact with <firstname> and <lastname>')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('add a new contact')
def add_contact(app, new_contact):
    app.contact.add(new_contact)


@then('the new contacts are equal to the old one')
def verify_contact_added(db, contacts, new_contact):
    old_contacts = contacts
    new_contacts = db.get_contacts()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('non-empty contacts')
def non_empty_contacts(app, db):
    if len(db.get_contacts()) == 0:
        app.contact.add(Contact(firstname='Alex', lastname='Murphy'))
    return db.get_contacts()


@given('random contact')
def random_contact(non_empty_contacts):
    return choice(non_empty_contacts)


@when('delete contact')
def delete_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@then('the new contacts are equal to the old contacts without the deleted contact')
def verify_contact_deleted(db, non_empty_contacts, random_contact):
    old_contacts = non_empty_contacts
    new_contacts = db.get_contacts()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@when('update firstname for contact')
def update_contact(app, random_contact):
    new_data = (Contact(firstname='Anne', lastname=random_contact.lastname))
    app.contact.update_by_id(random_contact.id, new_data)


@then('the new contacts are equal to the old contacts after updating')
def verify_contact_updated(db, non_empty_contacts, random_contact):
    old_contacts = non_empty_contacts
    index = old_contacts.index(random_contact)
    new_data = (Contact(firstname='Anne', lastname=random_contact.lastname))
    new_contacts = db.get_contacts()
    old_contacts[index] = new_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
