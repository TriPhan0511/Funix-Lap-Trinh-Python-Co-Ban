class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector: {{ x = {self.x} y = {self.y} }}'

    def __add__(self, another):
        return Vector(self.x + another.x, self.y + another.y)

    def __sub__(self, another):
        return Vector(self.x - another.x, self.y - another.y)


def main():
    a_vector = Vector(3, 7)
    b_vector = Vector(2, 8)

    # Output: Vector: { x = 5 y = 15 }
    print(a_vector + b_vector)

    # Output: Vector: { x = 1 y = -1 }
    print(a_vector - b_vector)


if __name__ == '__main__':
    main()
