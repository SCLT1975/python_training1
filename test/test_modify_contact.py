# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="qwerty")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data = Contact(name="oui", middle_name="uio", last_name="oiu", nick_name='oui',
                                   title='bnm', company='bnm', address='bnm', t_home='bnm', t_mobile='bnm', t_work='bnm',
                                   t_fax='111', email1='111', email2='111', email3='222', homepage='333', address2='333', home2='nnn', notes='nnnn', b_year=2010, a_year='1987')
    app.contact.modify_by_id(contact_data, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)






