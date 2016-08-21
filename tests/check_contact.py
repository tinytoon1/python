from model.contact import Contact


def test_check_contacts_info(app, orm):
    if len(orm.get_contacts()) == 0:
        app.contact.add(Contact(firstname='Alex', lastname='Murphy'))
    contacts_from_homepage = app.contact.get_contacts()
    contact_from_db = orm.get_contacts()
    assert sorted(contacts_from_homepage, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
