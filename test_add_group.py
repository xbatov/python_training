# -*- coding: utf-8 -*-
from application import Application
from group import Group

import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    group = Group(name="Group_1", header="Header of group_1", footer="Footer of Group_1")
    app.create_group(group)
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    group = Group(name="", header="", footer="")
    app.create_group(group)
    app.logout()
