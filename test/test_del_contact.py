# -*- coding: utf-8 -*-
from model._сontact import Contact

def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.Delete()
    app.session.logout()