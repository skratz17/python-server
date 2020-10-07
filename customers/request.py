CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct"
    },
    {
        "id": 2,
        "name": "Zap \"BrowserRouter\" Rowsdower",
        "address": "100 Main Street"
    },
    {
        "id": 3,
        "name": "Brom Grombo",
        "address": "200 Pain Street"
    },
    {
        "email": "jweckert17@gmail.com",
        "password": "test",
        "name": "Jacob Eckert",
        "id": 4
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    for customer in CUSTOMERS:
        if(customer["id"] == id):
            return customer

    return None