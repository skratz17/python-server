class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

if __name__ == '__main__':
    c = Customer('Jacob Eckert', '123 Main Street')
    print(c.name, c.address)