from model.group import Group
from model.contact import Contact
import random


def test_assign_contact_to_group(app, orm):
    if len(orm.get_contacts()) == 0:
        app.contact.add(Contact(firstname='add me to group'))
    if len(orm.get_groups()) == 0:
        app.group.add(Group(name='add to me'))

    db_groups = orm.get_groups()
    group = random.choice(db_groups)
    db_contacts = orm.get_contacts()
    contact = random.choice(db_contacts)
    contact_id = contact.id
    group_id = group.id

    app.contact.assign_to_group(contact_id, group_id)


def test_remove_contact_from_group(app, orm):
    if len(orm.get_contacts()) == 0:
        app.contact.add(Contact(firstname='assign me to group'))
    if len(orm.get_groups()) == 0:
        app.group.add(Group(name='assign to me'))

    db_groups = orm.get_groups()
    group = random.choice(db_groups)
    db_contacts = orm.get_contacts()
    contact = random.choice(db_contacts)

    group_id = group.id

    if len(orm.get_contacts_from_group(group_id)) == 0:
        contact_id = contact.id
        app.contact.assign_to_group(contact_id, group_id)
    else:
        contact = random.choice(orm.get_contacts_from_group(group_id))
        contact_id = contact.id

    app.contact.remove_from_group(contact_id, group_id)
