# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        return prefix + "".join(random.choice(symbols) for i in range (random.randrange(maxlen)))

testdata = [
        Contact(name=random_string("name", 10), middle_name=random_string("middle_name", 10), last_name=random_string("last_name", 10), nick_name=random_string("nick_name", 10),
                                   title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10), t_home=random_string("t_home", 10),
                                   t_mobile=random_string("t_mobile", 10), t_work=random_string("t_work", 10), t_fax=random_string("t_fax", 10),
                                   email1=random_string("email1", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
                                   homepage=random_string("homepage", 10), address2=random_string("address2", 10), home2=random_string("home2", 10),
                                   notes=random_string("notes", 10), b_year=random_string("b_year", 10), a_year=random_string("a_year", 10))
        for i in range(5)
        ]



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        assert len(old_contacts)+1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




