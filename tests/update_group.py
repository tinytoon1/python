# -*- coding: utf-8 -*-
from model.group import Group


def test_update_group_name(app):
    app.group.update(Group(name='empty group'))


def test_update_group_header(app):
    app.group.update(Group(header='empty header'))
