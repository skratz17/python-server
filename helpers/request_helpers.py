import urllib.parse

def get_next_id(LIST):
    if(len(LIST) == 0):
        return 1

    max_id = LIST[-1]["id"]
    return max_id + 1

def remove_item_by_id(LIST, id):
    found_index = -1

    for index, resource in enumerate(LIST):
        if resource["id"] == id:
            found_index = index

    if found_index >= 0:
        LIST.pop(found_index)

def replace_item_with_matching_id(LIST, id, replacement):
    for index, resource in enumerate(LIST):
        if resource["id"] == id:
            LIST[index] = replacement
            break

