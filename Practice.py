class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Coordinates(self.x / other.x, self.y / other.y)

    def __mul__(self, other):
        return Coordinates(self.x * other.x, self.y * other.y)


first = Coordinates(10, 12)
second = Coordinates(14, 18)

add = first + second
multiply = first * second
subtract = first - second
divide = first / second
print(first * second)
