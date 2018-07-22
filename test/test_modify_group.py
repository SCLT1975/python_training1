# -*- coding: utf-8 -*-
from model.group import Group
import random



def test_modify_group_py(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="123"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_data = Group(name="qwerty", header="123", footer="wqertyu")
    app.group.modify_by_id(group_data, group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

