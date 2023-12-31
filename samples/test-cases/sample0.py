# #
# Như đã giới thiệu ở trên, một Testcase sẽ bao gồm input, action và output mong đợi,
# để tạo một Testcase kiểm tra xem output có giống với output mong muốn hay không
# thì bạn có thể sử dụng test.testEqual hoặc assertEqual trong thư viện unittest, ví dụ như sau:

# import unittest


# class TestStringMethods(unittest.TestCase):
#     # Test function to test equality of two values
#     def test_nagative(self):
#         first_value = 'geeks'
#         second_value = 'geeks'
#         # second_value = 'gfg'
#         # Error message in case if test case got failed
#         message = 'First value and second value are not equal!'
#         # assertEqual to check equality of first value and second value
#         self.assertEqual(first_value, second_value, message)


# if __name__ == '__main__':
#     unittest.main()


# def update_counts(letters, counts_d):
#     for c in letters:
#         counts_d[c] = 1
#         if c in counts_d:
#             counts_d[c] = counts_d[c] + 1

def update_counts(letters, counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1


counts = {'a': 3, 'b': 2}
update_counts('aaab', counts)
