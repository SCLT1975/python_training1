# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(name="qwerty")))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="oui", middle_name="uio", last_name="oiu", nick_name='oui',
                                   title='bnm', company='bnm', address='bnm', t_home='bnm', t_mobile='bnm', t_work='bnm',
                                   t_fax='111', email1='111', email2='111', email3='222', homepage='333', address2='333', home2='nnn', notes='nnnn', b_year=2010, a_year='1987')
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





