# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name='first group'))
    app.group.delete()
