from helpers import get_next_id

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
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