from pytest_bdd import scenario
from .steps import *


@scenario('contacts.feature', 'add contact')
def test_add_contact():
    pass


@scenario('contacts.feature', 'delete contact')
def test_delete_contact():
    pass


@scenario('contacts.feature', 'update contact')
def test_update_contact():
    pass
