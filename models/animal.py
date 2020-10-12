class Animal:
    def __init__(self, id, name, breed, location_id, customer_id, status):
        self.id = id
        self.name = name
        self.breed = breed
        self.location_id = location_id
        self.customer_id = customer_id
        self.status = status

if __name__ == '__main__':
    a = Animal(1, 'Bo', 'Dawgg', 1, 2, 'Bein adorable')
    print(a.id, a.name, a.breed, a.location_id, a.customer_id, a.status)