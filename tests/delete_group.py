# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name='first group'))
    old_groups = app.group.get_groups()
    index = randrange(len(old_groups))
    app.group.delete(index)
    new_groups = app.group.get_groups()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
