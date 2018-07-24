from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(name="qwerty")))
    old_contacts = db.get_contact_list()
    group_list = db.get_group_list()
    group = random.choice(group_list)
    list_of_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    if len(list_of_contacts_in_group) == 0:
        contact = random.choice(old_contacts)
        app.contact.add_to_group(contact.id, group.id)
        list_of_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    contact_for_remove = random.choice(list_of_contacts_in_group)
    app.contact.del_from_group(contact_for_remove.id, group.id)
    list_of_contacts_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))
    list_of_contacts_not_in_group.index(contact_for_remove)