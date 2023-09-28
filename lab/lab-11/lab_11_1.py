"""lab 11.1"""

##
# Đề bài:
# Tạo một Class Bike bao gồm hai thuộc tính như sau

# color (string): Màu sắc của chiếc xe.
# price (float): Giá của chiếc xe.

# Sau đó, tạo hai Object Bike là testOne (color = 'blue', price = 89.99) và testTwo (color = 'purple', price = 25.0).

# Kiểm tra xem đoạn code đã hoạt động đúng chưa, nếu như output như sau thì bạn đã hoàn thành bài Lab này:

# blue 89.99
# purple 25.0
#


class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.color} {self.price}'


testOne = Bike(color='blue', price='89.99')
testTwo = Bike(color='purple', price='25.0')

print(testOne)
print(testTwo)
