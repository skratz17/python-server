EMPLOYEES = [
    {
        "name": "TEST CRAETION",
        "locationId": 2,
        "animalId": 3,
        "id": 1
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    for employee in EMPLOYEES:
        if(employee["id"] == id):
            return employee

    return None