from model._contact import Contact

def test_check_ui_db_contacts(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(
            firstname="firstname",
            middlename="middlename",
            lastname="lastname",
            address="address",
            homephone="111",
            mobilephone="222",
            workphone="333",
            email="email",
            email2="email2",
            email3="email3"
        ))
    ui_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert sorted(ui_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)