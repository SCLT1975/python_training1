from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="qwerty")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    group_list = db.get_group_list()
    group = random.choice(group_list)
    app.contact.add_to_group(contact.id, group.id)
    list_of_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    list_of_contacts_in_group.index(contact)