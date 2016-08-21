from model.group import Group
import random


def test_update_group_name(app, db, check_ui):
    if len(db.get_groups()) == 0:
        app.group.add(Group(name='first group'))
    old_groups = db.get_groups()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_data = Group(name='new name')
    new_data.id = group.id
    app.group.update_by_id(group.id, new_data)
    new_groups = db.get_groups()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = new_data
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups(), key=Group.id_or_max)
