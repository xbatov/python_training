import random
from fixture.orm import ORMFixture
from model._contact import Contact
from model._group import Group

def test_del_contact_in_group(app, orm):

    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    if not orm.get_group_list():
        app.group.create(Group(name="name", header="header", footer="footer"))


