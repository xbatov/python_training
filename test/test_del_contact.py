# -*- coding: utf-8 -*-
from model._сontact import Contact

def test_delete_contact(app):
    app.contact.delete()