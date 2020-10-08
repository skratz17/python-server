def get_next_id(LIST):
    if(len(LIST) == 0):
        return 1

    max_id = LIST[-1]["id"]
    return max_id + 1