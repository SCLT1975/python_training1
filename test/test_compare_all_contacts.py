# -*- coding: utf-8 -*-

from fixture.orm import ORMFixture
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_compare_all_contacts(app, db):
    db_contact_list = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    assert db_contact_list == contacts_from_home_page