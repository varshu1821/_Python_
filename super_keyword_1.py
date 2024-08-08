class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        base_area = super().area()
        rectangle_area = self.width * self.height
        return rectangle_area

rect = Rectangle(5,10)
print(rect.area())
