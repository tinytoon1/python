from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders
import re


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        address = Optional(str, column="address")
        homephone = Optional(str, column="home")
        mobilephone = Optional(str, column="mobile")
        workphone = Optional(str, column="work")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")

    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host=host, database=database, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_groups(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            converted = Contact(id=str(contact.id), firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                           address=contact.address.strip(), homephone=contact.homephone.strip(),
                                mobilephone=contact.mobilephone.strip(), workphone=contact.workphone.strip(),
                                email=contact.email.strip(), email2=contact.email2.strip(), email3=contact.email3.strip())
            converted.phones = self.merge_phones(converted)
            converted.emails = self.merge_emails(converted)
            return converted
        return list(map(convert, contacts))

    @db_session
    def get_contacts(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def merge_phones(self, contact):
        return "\n".join(filter(lambda x: x != "", map(lambda x: self.clear(x),
                                                       filter(lambda x: x is not None,
                                                              [contact.homephone, contact.mobilephone,
                                                               contact.workphone]))))

    def merge_emails(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                (filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

    def clear(self, info):
        return re.sub("[() -]", "", info)
