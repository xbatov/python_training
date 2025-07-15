# -*- coding: utf-8 -*-
from model._contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    day = random.randint(1, 31)
    return str(day)

def random_month():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])

def random_year():
    year = random.randint(1900, 2025)
    return str(year)

def random_phone_number():
    number = random.randint(1000000000, 9999999999)
    return str(number)

def generate_email():
    local_part = random_string("", 10)
    domain = "mail.ru"
    return f"{local_part}@{domain}"

testdata = [
    Contact(firstname="", middlename="", lastname="", nickname="",
            company="", title="", address="", homephone="", mobilephone="", fax= "",
            workphone="", email="", email2="", email3="",
            homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="")
] + [
    Contact(
        firstname=random_string("firstname: ", 10), middlename=random_string("middlename: ", 10),
        lastname=random_string("lastname: ", 10), nickname=random_string("nickname: ", 10),
        company=random_string("company: ", 10), title=random_string("title: ", 10),
        address=random_string("address: ", 20),
        homephone=random_phone_number(), mobilephone=random_phone_number(), workphone=random_phone_number(), fax=random_phone_number(),
        email=generate_email(), email2=generate_email(), email3=generate_email(),
        homepage=random_string("homepage: ", 10),
        bday=random_day(), bmonth=random_month(), byear=random_year(),
        aday=random_day(), amonth=random_month(), ayear=random_year()
    )
    for i in range(1)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)