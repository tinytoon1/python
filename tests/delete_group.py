# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name='first group'))
    old_groups = app.group.get_groups()
    app.group.delete()
    new_groups = app.group.get_groups()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

