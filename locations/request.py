from helpers import get_next_id, remove_item_by_id, replace_item_with_matching_id

LOCATIONS = [
  {
    "id": 1,
    "name": "Nashville North",
    "address": "8422 Johnson Pike"
  },
  {
    "id": 2,
    "name": "Nashville South",
    "address": "209 Emory Drive"
  }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    for location in LOCATIONS:
        if(location["id"] == id):
            return location
    
    return None

def create_location(location):
    location["id"] = get_next_id(LOCATIONS)

    LOCATIONS.append(location)
    return location

def update_location(id, location):
    replace_item_with_matching_id(LOCATIONS, id, location)

def delete_location(id):
    remove_item_by_id(LOCATIONS, id)