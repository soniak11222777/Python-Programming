import math

class Rectangle:
    
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return (self.width + self.height) * 2

def main():
    rectangle1= Rectangle(4,40)
    print("The width of the rectangle is",rectangle1.width,",the height is", rectangle1.height,",the area is", rectangle1.getArea(),",and the perimeter is", rectangle1.getPerimeter())
    rectangle2= Rectangle(3.5, 35.7)
    print("The width of the rectangle is",rectangle2.width,",the height is", rectangle2.height,",the area is", round(rectangle2.getArea(),2),",and the perimeter is", rectangle2.getPerimeter())
main()
