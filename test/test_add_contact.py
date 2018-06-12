# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.contact.create(Contact(name="qwerty", middle_name="123", last_name="wqertyu", nick_name='wer',
                                   title='brsf', company='ertw', address='qwer', t_home='dsaf', t_mobile='234', t_work='345',
                                   t_fax='345', email1='234', email2='534', email3='2134', homepage='5423', address2='3425', home2='gertgertg', notes='btertgwertgretg', b_year=2010, a_year='1987'))




