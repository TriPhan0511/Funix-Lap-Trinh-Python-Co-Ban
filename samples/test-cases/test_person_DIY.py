import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def test_set_name(self):
        david = Person()
        david_id = david.set_name('David')
        self.assertEqual(david_id, 0)
        self.assertEqual(len(david.names), 1)
        self.assertEqual(david.names, ['David'])
        self.assertNotEqual(len(david.names), 0)
        self.assertNotEqual(david.names, [])

        rose = Person()
        rose_id = rose.set_name('Rose')
        self.assertEqual(rose_id, 1)
        self.assertEqual(len(rose.names), 2)
        self.assertEqual(rose.names, ['David', 'Rose'])
        self.assertNotEqual(len(rose.names), 1)
        self.assertNotEqual(rose.names, [])

        self.assertNotEqual(david.names, ['David'])


if __name__ == '__main__':
    unittest.main()
