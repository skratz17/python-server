def get_next_id(LIST):
    if(len(LIST) == 0):
        return 1

    max_id = LIST[-1]["id"]
    return max_id + 1

def parse_url(path):
    path_params = path.split("/")
    resource = path_params[1]
    id = None

    try:
        id = int(path_params[2])
    except IndexError:
        pass
    except ValueError:
        pass

    return (resource, id) # This is called a "tuple