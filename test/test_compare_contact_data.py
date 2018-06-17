# -*- coding: utf-8 -*-

import re
from random import randrange

def test_compare_contact_on_home_and_edit(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    compiration_info_from_home_page = [contact_from_home_page.all_phones_from_home_page, contact_from_home_page.all_emails_from_home_page, contact_from_home_page.name, contact_from_home_page.last_name, contact_from_home_page.address]
    megred_phones = merge_phones_like_on_home_page(contact_from_edit_page)
    merged_emails = merge_emails_like_on_home_page(contact_from_edit_page)
    compiration_info_from_edit_page = [megred_phones, merged_emails, contact_from_edit_page.name, contact_from_edit_page.last_name, contact_from_edit_page.address]
    assert compiration_info_from_home_page == compiration_info_from_edit_page



def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    compiration_info_from_home_page = [contact_from_view_page.t_home, contact_from_view_page.t_mobile,
                                       contact_from_view_page.t_work, contact_from_view_page.home2]
    compiration_info_from_edit_page = [contact_from_edit_page.t_home, contact_from_edit_page.t_mobile,
                                       contact_from_edit_page.t_work, contact_from_edit_page.home2]
    assert  compiration_info_from_home_page == compiration_info_from_edit_page


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.t_home, contact.t_mobile, contact.t_work,  contact.home2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))