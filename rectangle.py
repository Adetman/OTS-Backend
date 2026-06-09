#Rectangle Class with length and width
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

#Create an instance of the Rectangle class
my_rectangle = Rectangle(5, 3)

#Print the area of the rectangle
print(my_rectangle.area())

