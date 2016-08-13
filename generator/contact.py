# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as error:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_data(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(max_len)))


test_data = [Contact(firstname="", lastname="", address="", homephone="",
                     mobilephone="", workphone="", email="", email2="", email3="")] + \
            [Contact(firstname=random_data("firstname", 10), lastname=random_data("lastname", 10),
                     address=random_data("address", 10), homephone=random_data("homephone", 10),
                     mobilephone=random_data("mobilephone", 10), workphone=random_data("workphone", 10),
                     email=random_data("email", 10), email2=random_data("email2", 10), email3=random_data("email3", 10))
                for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
