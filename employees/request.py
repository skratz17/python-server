from helpers import get_next_id, remove_item_by_id, replace_item_with_matching_id

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

def update_employee(id, employee):
    replace_item_with_matching_id(EMPLOYEES, id, employee)

def delete_employee(id):
    remove_item_by_id(EMPLOYEES, id)