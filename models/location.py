class Location:
    def __init__(self, name, address):
        self.name = name
        self.address = address

if __name__ == '__main__':
    l = Location('Nashville North', '123 Pain Street')
    print(l.name, l.address)