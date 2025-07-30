from model._contact import Contact
import re

def test_check_ui_db_contacts(app, db):

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="", title="",
                                   company="", address="address", homephone="111", mobilephone="222", workphone="333", fax="", email="email",
                                   email2="email2", email3="email3", homepage="", byear="1900", ayear="2000", bday="24", bmonth="May",
                                   aday="14", amonth="December"))

    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)

    for i in range(len(ui_contacts)):
        assert ui_contacts[i].firstname == clear_names(db_contacts[i].firstname)
        assert ui_contacts[i].lastname == clear_names(db_contacts[i].lastname)
        assert ui_contacts[i].address == db_contacts[i].address
        assert ui_contacts[i].all_phones_from_home_page == merge_phones_like_on_home_page(db_contacts[i])
        assert ui_contacts[i].all_emails_from_home_page == merge_emails_like_on_home_page(db_contacts[i])

def clear_names(string):
    if string and string[-1] == " ":
        return string[0:-1]
    else:
        return string

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join([contact.email, contact.email2, contact.email3])