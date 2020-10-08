from helpers import get_next_id, remove_item_by_id, replace_item_with_matching_id

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]

def get_all_animals():
    return ANIMALS

def get_single_animal(id):
    requested_animal = None

    # each animal variable here is a "dictionary" in Python, basically analogous to an "object" in JS
    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    animal["id"] = get_next_id(ANIMALS)

    ANIMALS.append(animal)
    return animal

def update_animal(id, new_animal):
    replace_item_with_matching_id(ANIMALS, id, new_animal)

def delete_animal(id):
    remove_item_by_id(ANIMALS, id)