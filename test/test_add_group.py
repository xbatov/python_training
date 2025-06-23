# -*- coding: utf-8 -*-
import pytest
from model._group import Group
from fixture._application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    group = Group(name="Group_1", header="Header of group_1", footer="Footer of Group_1")
    app.group.create_group(group)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    group = Group(name="", header="", footer="")
    app.group.create_group(group)
    app.session.logout()