from model.contact import Contact


def test_add_contact(app, orm, check_ui, json_contacts):
    contact = json_contacts
    old_contacts = orm.get_contacts()
    app.contact.add(contact)
    new_contacts = orm.get_contacts()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts(), key=Contact.id_or_max)
