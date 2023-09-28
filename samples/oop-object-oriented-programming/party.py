class PartyAnimal:
    def __init__(self, name):
        self.name = name
        self.x = 0
        print(f'{self.name} constructed.')

    def party(self):
        self.x += 1
        print(f'{self.name} count {self.x}')
