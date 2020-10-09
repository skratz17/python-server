class Employee:
    def __init__(self, name, locationId, animalId):
        self.name = name
        self.locationId = locationId
        self.animalId = animalId

if __name__ == '__main__':
    e = Employee('Worker Man', 1, 2)
    print(e.name, e.locationId, e.animalId)