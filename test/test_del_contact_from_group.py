import random
from fixture.orm import ORMFixture
from model._contact import Contact
from model._group import Group

orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")


def test_del_contact_in_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        if len(orm.get_contact_list()) == 0:
            app.contact.create(Contact(
                firstname="firstname", middlename="middlename", lastname="lastname", nickname="", title="",
                company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
                email3="", homepage="", byear="1900", ayear="2000", bday="24", bmonth="May", aday="14",
                amonth="December"))
        contact = random.choice(orm.get_contact_list())
        try:
            app.contact.add_contact_by_id_in_group(contact, group)
        except Exception as e:
            print(f"Ошибка при добавлении контакта в группу: {str(e)}")

    contacts_in_group = orm.get_contacts_in_group(group)
    contact_to_remove = random.choice(contacts_in_group)

    try:
        app.contact.delete_contact_by_id_from_group(contact_to_remove, group)
    except Exception as e:
        print(f"Ошибка при удалении контакта из группы: {str(e)}")

    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_to_remove not in new_contacts_in_group
    contacts_in_group.remove(contact_to_remove)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
