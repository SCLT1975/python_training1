
# -*- coding: utf-8 -*-

from model.group import Group

def test_test_del_group(app):
        if app.group.count() == 0:
                app.group.create(Group(name="123"))
        app.group.delete()

