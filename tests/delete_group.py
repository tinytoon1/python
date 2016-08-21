from model.group import Group
import random


def test_delete_group(app, orm, check_ui):
    if len(orm.get_groups()) == 0:
        app.group.add(Group(name='first group'))
    old_groups = orm.get_groups()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = orm.get_groups()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups(), key=Group.id_or_max)
