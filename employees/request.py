from helpers import get_next_id

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

def create_employee(employee):
    employee["id"] = get_next_id(EMPLOYEES)

    EMPLOYEES.append(employee)
    return employee