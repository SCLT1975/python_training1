
# -*- coding: utf-8 -*-

from model.group import Group

def test_test_del_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="123"))
        old_groups = app.group.get_group_list()
        app.group.delete()
        assert len(old_groups) - 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[0:1] = []
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

