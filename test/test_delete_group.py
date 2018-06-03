
# -*- coding: utf-8 -*-


def test_test_del_group(app):
        app.session.login(username="admin", password="secret")
        app.group.delete()
        app.session.logout()
