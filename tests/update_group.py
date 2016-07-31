# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.add(Group(name='first group'))
    old_groups = app.group.get_groups()
    index = randrange(len(old_groups))
    group = Group(name='new name')
    group.id = old_groups[index].id
    app.group.update(index, group)
    new_groups = app.group.get_groups()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_update_group_header(app):
#    if app.group.count() == 0:
#        app.group.add(Group(name='first group'))
#    old_groups = app.group.get_grouplist()
#    app.group.update(Group(header='new header'))
#    new_groups = app.group.get_grouplist()
#    assert len(old_groups) == len(new_groups)
