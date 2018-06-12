# -*- coding: utf-8 -*-
from model.group import Group




def test_test_add_group_py(app):
    app.group.modify(Group(name="qwerty", header="123", footer="wqertyu"))
