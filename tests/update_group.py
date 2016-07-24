# -*- coding: utf-8 -*-
from model.group import Group


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.add(Group(name='first group'))
    app.group.update(Group(name='new name'))


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.add(Group(name='first group'))
    app.group.update(Group(header='new header'))
