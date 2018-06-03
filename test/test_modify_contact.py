# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.modify(Contact(name="oui", middle_name="uio", last_name="oiu", nick_name='oui',
                                   title='bnm', company='bnm', address='bnm', t_home='bnm', t_mobile='bnm', t_work='bnm',
                                   t_fax='111', email1='111', email2='111', email3='222', homepage='333', address2='333', home2='nnn', notes='nnnn', b_year=2010, a_year='1987'))
        app.session.logout()



