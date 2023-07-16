class Rectangle() :
    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def get_area(self) :
        return self.width * self.height
    
    def get_perimeter(self) :
        return 2 * (self.width + self.height)
    

rectangle = Rectangle(4 , 5)
print(rectangle.get_area())
print(rectangle.get_perimeter())
