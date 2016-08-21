from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_groups()
    app.group.add(group)
    new_groups = db.get_groups()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups(), key=Group.id_or_max)
