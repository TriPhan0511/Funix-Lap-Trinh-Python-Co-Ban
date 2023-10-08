# #
# Link:
# https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example
#


class Person:
    names = []

    def set_name(self, user_name):
        self.names.append(user_name)
        return len(self.names) - 1

    def get_name(self, id):
        if id >= len(self.names):
            return 'There is no such user'
        else:
            return self.names[id]


if __name__ == '__main__':
    person = Person()
    print(f'User Abbas has been added with id {person.set_name("Abbas")}')
    print(f'User associated with id 0 is {person.get_name(0)}')
    # User Abbas has been added with id 0
    # User associated with id 0 is Abbas
