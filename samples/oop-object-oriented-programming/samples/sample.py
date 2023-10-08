# =======  Classes as types =======

# class PartyAnimal:
#     x = 0

#     def party(self):
#         self.x += 1
#         print(f'So far {self.x}')


# an = PartyAnimal()

# # an.party()  # So far 1
# # an.party()  # So far 2
# # an.party()  # So far 3
# # PartyAnimal.party(an)  # So far 4

# print(dir(an))
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# #  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']

# print(type(an))  # <class '__main__.PartyAnimal'>
# print(type(an.x))  # <class 'int'>
# print(type(an.party))  # <class 'method'>

# =======  Object lifecycle =======

# class PartyAnimal:
#     x = 0

#     def __init__(self):
#         print('I am constructed.')

#     def party(self):
#         self.x += 1
#         print(f'So far {self.x}')

#     def __del__(self):
#         print(f'I am desctructed {self.x}')


# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print(f'an contains {an}')
# # I am constructed.
# # So far 1
# # So far 2
# # I am desctructed 2
# # an contains 42

# ======= Multiple instances =======

class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(f'{self.name} constructed.')

    def party(self):
        self.x += 1
        print(f'{self.name} party count {self.x}')


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
# Sally constructed.
# Jim constructed.
# Sally party count 1
# Jim party count 1
# Sally party count 2
