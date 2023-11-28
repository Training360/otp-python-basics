def find_item(id: int, items: list) -> dict | None:
    for item in items:
        if item['id'] == id:
            return item


def remove_item(id: int, items: list) -> None:
    item = find_item(id, items)
    if item is not None:
        items.remove(item)


def update_item(id: int, updated_item: dict, items: list) -> dict | None:
    # find updatable item
    item = find_item(id, items)
    # if item exists
    if item is not None:
        # get the index
        i = items.index(item)
        items[i].update(updated_item)
        return items[i]


def create_item(item: dict, items: list) -> dict:
    # id-t generáljátok le, az utolsó elem id-ja + 1
    new_item = {'id': items[-1]['id'] + 1}
    new_item.update(item)
    items.append(new_item)
    return items[-1]
