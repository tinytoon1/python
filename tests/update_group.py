# -*- coding: utf-8 -*-
from model.group import Group


def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update(Group(name='empty group'))
    app.session.logout()
