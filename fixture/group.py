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
        self.groups_cache = None

    def delete(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.groups_cache = None

    def update(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.open_to_edit(index)
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.groups_cache = None

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

    def select_group(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    groups_cache = None

    def get_groups(self):
        if self.groups_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.groups_cache = []
            for entry in range(self.count()):
                self.groups_cache.append(self.get_info_from_edit_page(entry))
        return list(self.groups_cache)

    def open_to_edit(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        wd.find_element_by_name("edit").click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.open_to_edit(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        name = wd.find_element_by_name("group_name").get_attribute("value")
        header = wd.find_element_by_name("group_header").get_attribute("value")
        footer = wd.find_element_by_name("group_footer").get_attribute("value")
        return Group(id=id, name=name, header=header, footer=footer)
