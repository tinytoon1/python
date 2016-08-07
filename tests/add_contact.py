# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_data(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(max_len)))


test_data = [Contact(firstname="", lastname="", address="", homephone="",
                     mobilephone="", workphone="", email="", email2="", email3="")] + \
            [Contact(firstname=random_data("firstname", 10), lastname=random_data("lastname", 10),
                     address=random_data("address", 10), homephone=random_data("homephone", 10),
                     mobilephone=random_data("mobilephone", 10), workphone=random_data("workphone", 10),
                     email=random_data("email", 10), email2=random_data("email2", 10), email3=random_data("email3", 10))
                for i in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts()
    app.contact.add(contact)
    new_contacts = app.contact.get_contacts()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
