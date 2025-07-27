# -*- coding: utf-8 -*-
from model._group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_modify_group_name"))
    old_groups = db.get_group_list()
    group = Group(name="New group")
    group_id = (random.choice(old_groups)).id
    app.group.modify_group_by_id(group_id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)