# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.add(Group(name="old", header="old header", footer="old footer"))


#def test_add_empty_group(app):
#    app.group.add(Group(name="", header="", footer=""))
