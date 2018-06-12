# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(name="qwerty", middle_name="123", last_name="wqertyu", nick_name='wer',
                                   title='brsf', company='ertw', address='qwer', t_home='dsaf', t_mobile='234', t_work='345',
                                   t_fax='345', email1='234', email2='534', email3='2134', homepage='5423', address2='3425', home2='gertgertg', notes='btertgwertgretg', b_year=2010, a_year='1987')
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




