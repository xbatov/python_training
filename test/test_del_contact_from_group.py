import random
from model._contact import Contact
from model._group import Group

def test_del_contact_from_group(app, orm):
    # 1. Подготовка данных - гарантируем наличие группы
    if not orm.get_group_list():
        app.group.create(Group(name="Test group"))
    group = random.choice(orm.get_group_list()) # Берем группу

    # 2. Гарантируем наличие контакта в группе
    contacts_in_group = orm.get_contacts_in_group(group)
    if not contacts_in_group:
        # Если нет контактов в группе - добавляем
        if not orm.get_contact_list():
            # Гарантируем наличие контакта в базе
            app.contact.create(Contact(
                    firstname="firstname", middlename="", lastname="", nickname="", title="",
                    company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
                    email3="", homepage="", byear="1900", ayear="2000", bday="24", bmonth="May", aday="14",
                    amonth="December"))
        # Берем контакт и добавляем в пустую группу
        contact_to_add = orm.get_contact_list()[0]
        app.contact.add_contact_by_id_in_group(contact_to_add, group)
        contacts_in_group = orm.get_contacts_in_group(group)

    # 3. Выбираем случайный контакт для удаления
    contact_to_delete = random.choice(contacts_in_group)

    # 4. Удаляем контакт из группы
    app.contact.delete_contact_by_id_from_group(contact_to_delete, group)

    # 5. Проверки
    updated_contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_to_delete not in updated_contacts_in_group
    assert len(updated_contacts_in_group) == len(contacts_in_group) - 1