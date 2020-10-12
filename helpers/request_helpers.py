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

def parse_url(path):
    path_params = path.split("/")
    resource = path_params[1]

    # URL includes query string - parse it and return tuple of resource name, 
    # query string param, and value for that param in the query string
    if "?" in resource:
        resource, param = resource.split("?")
        key, value = param.split("=")

        value = urllib.parse.unquote(value)

        return ( resource, key, value )

    # Otherwise, it is just a request for either all items of a particular resource,
    # or a single item by ID
    else:
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

    return (resource, id) # This is called a "tuple