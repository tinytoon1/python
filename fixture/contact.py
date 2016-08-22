# -*- coding: utf-8 -*-
from model.contact import Contact
import re


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

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_homepage()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_homepage()
        self.contacts_cache = None

    def update(self, index, contact):
        wd = self.app.wd
        self.open_homepage()
        self.open_to_edit(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_homepage()
        self.contacts_cache = None

    def update_by_id(self, id, contact):
        wd = self.app.wd
        self.open_homepage()
        self.open_to_edit_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_homepage()
        self.contacts_cache = None

    def fill_contact_form(self, contact):
        self.update_field("firstname", contact.firstname)
        self.update_field("lastname", contact.lastname)
        self.update_field("address", contact.address)
        self.update_field("home", contact.homephone)
        self.update_field("mobile", contact.mobilephone)
        self.update_field("work", contact.workphone)
        self.update_field("email", contact.email)
        self.update_field("email2", contact.email2)
        self.update_field("email3", contact.email3)

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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    contacts_cache = None

    def get_contacts(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contacts_cache = []
            entries = wd.find_elements_by_name("entry")
            for element in entries:
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                phones = cells[5].text
                emails = cells[4].text
                self.contacts_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                   phones=phones, emails=emails))
        return list(self.contacts_cache)

    def open_to_edit(self, index):
        wd = self.app.wd
        self.open_homepage()
        entry = wd.find_elements_by_name("entry")[index]
        cell = entry.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_homepage()
        entries = wd.find_elements_by_name("entry")
        for element in entries:
            cells = element.find_elements_by_tag_name("td")
            if cells[0].find_element_by_tag_name("input").get_attribute("value") == str(id):
                cell = cells[7]
                cell.find_element_by_tag_name("a").click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.open_to_edit(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilphone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilphone,
                       workphone=workphone, email=email, email2=email2, email3=email3)

    def clear(self, info):
        return re.sub("[() -]", "", info)

    def merge_phones(self, contact):
        return "\n".join(filter(lambda x: x != "", map(lambda x: self.clear(x),
                        filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone]))))

    def merge_emails(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
