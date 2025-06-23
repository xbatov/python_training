# -*- coding: utf-8 -*-
import pytest
from _application import Application
from _сontact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    contact = Contact(firstname="Donald", middlename="Jr", lastname="Trump", nickname="POTUS", title="CEO",
                      company="White house", address="Washington DC", homephone="+11002050", mobilephone="+11002051",
                      workphone="+11002052", fax="none", email="donald@usa.gov", email2="donald2@usa.gov",
                      email3="donald3@usa.gov", homepage="usa.gov", byear="1950", ayear="2025", bday="4",
                      bmonth="November", aday="4", amonth="October")
    app.Add_new_contact(contact)
    app.logout()