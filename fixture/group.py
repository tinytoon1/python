# -*- coding: utf-8 -*-
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def add(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def update(self, group):
        wd = self.app.wd
        # go to another page
        wd.find_element_by_link_text("home").click()
        # return
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.open_groups_page()

    def fill_group_form(self, group):
        self.update_field("group_name", group.name)
        self.update_field("group_header", group.header)
        self.update_field("group_footer", group.footer)

    def update_field(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def get_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            name = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=name, id=id))
        return groups
