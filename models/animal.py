class Animal:
    def __init__(self, id, name, species, locationId, customerId, status):
        self.id = id
        self.name = name
        self.species = species
        self.locationId = locationId
        self.customerId = customerId
        self.status = status

if __name__ == '__main__':
    a = Animal(1, 'Bo', 'Dawgg', 1, 2, 'Bein adorable')
    print(a.id, a.name, a.species, a.locationId, a.customerId, a.status)