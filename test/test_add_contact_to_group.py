import random
from fixture.orm import ORMFixture
from model._contact import Contact
from model._group import Group

def test_add_contact_in_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if not orm.get_group_list():
        app.group.create(Group(name="name", header="header", footer="footer"))
    group = orm.get_group_list()[0]
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
    if not contacts_not_in_group:
        app.contact.create(Contact(
            firstname="firstname", middlename="", lastname="", nickname="", title="",
            company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
            email3="", homepage="", byear="1900", ayear="2000", bday="24", bmonth="May", aday="14",
            amonth="December"))
    contacts_not_in_group = orm.get_contacts_not_in_group(Group(id=group.id))
    contact_to_add = contacts_not_in_group[0]
    app.contact.add_contact_by_id_in_group(contact_to_add, group)
    contacts_in_group = orm.get_contacts_in_group((Group(id=group.id)))
    assert contact_to_add in contacts_in_group
