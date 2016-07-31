# -*- coding: utf-8 -*-
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.open_homepage()
        self.contacts_cache = None

    def delete(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_homepage()
        self.contacts_cache = None

    def update(self, index, contact):
        wd = self.app.wd
        self.open_homepage()
        # click on "edit" for the first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(index+2)+"]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_homepage()
        self.contacts_cache = None

    def fill_contact_form(self, contact):
        self.update_field("firstname", contact.firstname)
        self.update_field("lastname", contact.lastname)
        self.update_field("company", contact.company)
        self.update_field("address", contact.address)
        self.update_field("mobile", contact.mobile)

    def update_field(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchform")) > 0):
            wd.find_element_by_link_text("home").click()

    def select_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    contacts_cache = None

    def get_contacts(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contacts_cache = []
            entries = wd.find_elements_by_name("entry")
            tr = 2  # row with first entry
            for element in entries:
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(tr)+"]/td[3]").text
                lastname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(tr)+"]/td[2]").text
                self.contacts_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
                tr += 1  # next entry
        return list(self.contacts_cache)
