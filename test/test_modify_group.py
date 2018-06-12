# -*- coding: utf-8 -*-
from model.group import Group




def test_modify_group_py(app):
    if app.group.count() == 0:
        app.group.create(Group(name="123"))
    old_groups = app.group.get_group_list()
    group = Group(name="qwerty", header="123", footer="wqertyu")
    group.id = old_groups[0].id
    app.group.modify(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
