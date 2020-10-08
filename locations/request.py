from helpers import get_next_id

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