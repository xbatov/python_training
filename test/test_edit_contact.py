# -*- coding: utf-8 -*-
from model._сontact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                      company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
                      email3="", homepage="", byear="1900", ayear="2000", bday="24", bmonth="May", aday="14", amonth="December"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Donald2", middlename="Jr2", lastname="Trump2", nickname="POTUS2", title="CEO2",
                      company="White house2", address="Washington DC2", homephone="+110020502", mobilephone="+110020512",
                      workphone="+110020522", fax="none2", email="donald@usa.gov2", email2="donald2@usa.gov2",
                      email3="donald3@usa.gov2", homepage="usa.gov2", byear="1952", ayear="2024", bday="24", bmonth="May", aday="14", amonth="December",
                      id=old_contacts[index].id)
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)