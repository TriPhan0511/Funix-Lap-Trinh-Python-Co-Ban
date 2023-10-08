# #
# Link:
# https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example
# Now, let’s learn how to code for unit testing.
# An individual testcase is created by subclassing unittest.TestCase.
# By overriding or adding appropriate functions, we can add logic to test.
# The following code will be succeeded if a is equals to b.

import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some222'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_string_not_equal(self):
        a = 'hello'
        b = 'bonjour'
        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
