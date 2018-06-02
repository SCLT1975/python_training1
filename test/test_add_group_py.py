# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture




    
def test_test_add_group_py(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="qwerty", header="123", footer="wqertyu"))
        app.session.logout()


def test_test_add_empty_group_py(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
