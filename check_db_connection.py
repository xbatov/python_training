from fixture.orm import ORMFixture
from model._group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    l = db.get_contacts_not_in_group(Group(id="111"))
    for item in l:
        print(item)
    print(f"Total: {len(l)}")

finally:
    pass