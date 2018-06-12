
# -*- coding: utf-8 -*-

from model.group import Group

def test_test_del_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="123"))
        old_groups = app.group.get_group_list()
        app.group.delete()
        new_groups = app.group.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups[0:1] = []
        assert old_groups == new_groups

