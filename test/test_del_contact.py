# -*- coding: utf-8 -*-
from model._сontact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                      company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
                      email3="", homepage="", byear="1900", ayear="2000", bday="24", bmonth="May", aday="14", amonth="December"))
    app.contact.delete()