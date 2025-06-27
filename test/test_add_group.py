# -*- coding: utf-8 -*-
from model._group import Group


def test_add_group(app):
    group = Group(name="Group_1", header="Header of group_1", footer="Footer of Group_1")
    app.group.create(group)


def test_add_empty_group(app):
    group = Group(name="", header="", footer="")
    app.group.create(group)