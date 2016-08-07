# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_data(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(max_len)))


test_data = [Group(name="", header="", footer="")] + \
            [Group(name=random_data("name", 10), header=random_data("header", 20), footer=random_data("footer", 20))
                for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_groups()
    app.group.add(group)
    new_groups = app.group.get_groups()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
