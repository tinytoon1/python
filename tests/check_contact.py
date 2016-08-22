from model.contact import Contact


def test_check_contacts_info(app, orm):
    if len(orm.get_contacts()) == 0:
        app.contact.add(Contact(firstname='Alex', lastname='Murphy'))
    contacts_from_homepage = sorted(app.contact.get_contacts(), key=Contact.id_or_max)
    contacts_from_db = sorted(orm.get_contacts(), key=Contact.id_or_max)
    assert len(contacts_from_homepage) == len(contacts_from_db)
    for i in range(len(contacts_from_db)):
        assert contacts_from_homepage[i].id == contacts_from_db[i].id
        assert contacts_from_homepage[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_homepage[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_homepage[i].address == contacts_from_db[i].address
        assert contacts_from_homepage[i].phones == contacts_from_db[i].phones
        assert contacts_from_homepage[i].emails == contacts_from_db[i].emails
