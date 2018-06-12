# -*- coding: utf-8 -*-
from model.group import Group




def test_test_add_group_py(app):
    if app.group.count() == 0:
        app.group.create(Group(name="123"))
    app.group.modify(Group(name="qwerty", header="123", footer="wqertyu"))
