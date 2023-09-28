"""lab 11.2"""

##
# Đề bài:
# Tạo một Class AppleBasket bao gồm hai thuộc tính như sau

# apple_color (string): Màu sắc của quả táo.
# apple_quantity (int): Số lượng táo trong giỏ.

# Sau đó, bạn cần tạo một Class Method increase sử dụng để tăng giá trị của thuộc tính apple_quantity` thêm 1.
# Cuối dùng, bạn cần thiết kế để khi in Object được tạo thì sẽ có format như sau A basket of [quantity] [color] apples.

# Kiểm tra xem đoạn code đã hoạt động đúng chưa, nếu như output như sau thì bạn đã hoàn thành bài Lab này:

# A basket of 4 red apples.
# A basket of 5 red apples.
#


class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self) -> str:
        return f'A basket of {self.apple_quantity} {self.apple_color} apples.'


def main():
    testOne = AppleBasket('red', 4)
    print(testOne)
    testOne.increase()
    print(testOne)
    # Output:
    # A basket of 4 red apples.
    # A basket of 5 red apples.


if __name__ == '__main__':
    main()
