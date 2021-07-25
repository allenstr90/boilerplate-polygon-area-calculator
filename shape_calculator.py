class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        res = ''.ljust(self.width, '*')
        for y in range(1, self.height):
            res += f'\n{"".ljust(self.width, "*")}'
        return res + '\n'

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.side = length

    def set_side(self, side):
        self.side = self.height = self.width = side

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

    def __str__(self):
        return f'Square(side={self.side})'
