# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture




    
def test_test_add_group_py(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="qwerty", header="123", footer="wqertyu"))
        app.logout()


def test_test_add_empty_group_py(app):
        app.login(username="admin", password="secret")
        app.open_groups_page()
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
