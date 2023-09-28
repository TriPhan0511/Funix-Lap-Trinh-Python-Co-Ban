class Animal:
    type = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0

    def __str__(self) -> str:
        return f'Type: {self.type} - Name: {self.name} - Age: {self.age}'

    def feed(self):
        self.hunger += 1


class Cat(Animal):
    type = 'Cat'


class Dog(Animal):
    type = 'Dog'

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def __str__(self):
        return f'{super().__str__()} - Gender: {self.gender}'


class Bird(Animal):
    type = 'Bird'

    def fly(self):
        print(f"My name's {self.name}. I can fly.")


lily = Cat('Lily', 5)
print(lily)
mino = Dog('Mino', 10, 'male')
print(mino)
rose = Bird('Rose', 3)
rose.fly()
# Output:
# Type: Cat - Name: Lily - Age: 5
# Type: Dog - Name: Mino - Age: 10 - Gender: male
# My name's Rose. I can fly.
