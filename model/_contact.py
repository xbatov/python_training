# -*- coding: utf-8 -*-
from sys import maxsize

class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, title = None, company = None,
                 address = None, homephone = None, mobilephone = None, workphone = None, fax = None, email = None,
                 email2 = None, email3 = None, homepage = None, byear = None, ayear = None, bday = None,
                 bmonth = None, aday = None, amonth = None, id = None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.address = address
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.bday = bday
        self.bmonth = bmonth
        self.aday = aday
        self.amonth = amonth
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname == other.firstname) and (self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize