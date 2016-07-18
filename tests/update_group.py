# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first(Group(name='empty group', header='', footer=''))
    app.session.logout()
