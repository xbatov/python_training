# -*- coding: utf-8 -*-
from model._сontact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    contact = Contact(firstname="Donald2", middlename="Jr2", lastname="Trump2", nickname="POTUS2", title="CEO2",
                      company="White house2", address="Washington DC2", homephone="+110020502", mobilephone="+110020512",
                      workphone="+110020522", fax="none2", email="donald@usa.gov2", email2="donald2@usa.gov2",
                      email3="donald3@usa.gov2", homepage="usa.gov2", byear="1952", ayear="2024", bday="24", bmonth="May", aday="14", amonth="December")
    app.contact.edit(contact)
    app.session.logout()