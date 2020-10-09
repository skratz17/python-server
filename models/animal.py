class Animal:
    def __init__(self, name, species, locationId, customerId, status):
        self.name = name
        self.species = species
        self.locationId = locationId
        self.customerId = customerId
        self.status = status

if __name__ == '__main__':
    a = Animal('Bo', 'Dawgg', 1, 2, 'Bein adorable')
    print(a.name, a.species, a.locationId, a.customerId, a.status)