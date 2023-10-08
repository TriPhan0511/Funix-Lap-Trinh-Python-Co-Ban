import unittest
from person import Person


# class TestPerson(unittest.TestCase):
#     person = Person()  # Instantiate a Person object
#     ids = []
#     names = []

#     def test_set_name(self):
#         for i in range(4):
#             name = f'name {i}'
#             self.names.append(name)
#             id = self.person.set_name(name)  # Obtain id from function return
#             self.assertIsNotNone(id)
#             self.ids.append(id)

#         self.assertEqual(len(self.ids), 4)
#         self.assertEqual(len(self.names), 4)
#         self.assertNotEqual(len(self.ids), 0)
#         self.assertNotEqual(len(self.names), 0)

#         self.assertListEqual(self.ids, [0, 1, 2, 3])
#         self.assertListEqual(
#             self.names, ['name 0', 'name 1', 'name 2', 'name 3',])

class TestPerson(unittest.TestCase):
    ids = []
    names = []
    people = []

    def collect_ids_and_names(self, person):
        for i in range(4):
            name = f'name {i}'
            self.names.append(name)
            self.ids.append(person.set_name(name))
            self.people.append(person)

    def test_set_name(self):
        person = Person()
        self.collect_ids_and_names(person)

        self.assertEqual(len(self.ids), 4)
        self.assertEqual(len(self.names), 4)
        self.assertNotEqual(len(self.ids), 0)
        self.assertNotEqual(len(self.names), 0)

        self.assertListEqual(self.ids, [0, 1, 2, 3])
        self.assertListEqual(
            self.names, ['name 0', 'name 1', 'name 2', 'name 3',])

        self.assertEqual(len(self.people), 4)

        for p in self.people:
            self.assertIsNotNone(p)
            self.assertIsInstance(p, Person)

    def test_get_name(self):
        p = Person()
        self.collect_ids_and_names(p)
        
        for id in self.ids:


if __name__ == '__main__':
    unittest.main()
