class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


c = Rectangle(5, 9)
print(f"The area of the rectangle is: {c.area()}")
