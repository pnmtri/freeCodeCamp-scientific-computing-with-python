class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # set_width() and set_height() are later used when we want to change values of width or height with less efforts than using bland assignment operation e.g. instance_name.width = ? , etc.
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Picture the basic simulated format of the shape using '*'s
    def get_picture(self):
        if 50 < (self.width or self.height):
            return 'Too big for picture.'
        return ('*'*self.width + '\n')*self.height
    
    # Calculate how many component shapes fit inside the mother shape
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
    
    # Return the measuring parameters of the initial shape
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    

###
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    # The 2 following blocks of method are to overwrite the super class Rectangle width and height to obey the rule of a square having equal sides
    def set_width(self, width):
        self.set_side(width) # Use set_side() method created previously
    def set_height(self, height):
        self.set_side(height) # Similarly as above

    # Return the measuring parameters of the initial shape
    def __str__(self):
        return f"Square(side={self.width})"


# SOME TESTS
rect = Rectangle(10, 5)
print(rect.get_area())         # 50
rect.serimt_height(3)
print(rect.get_peeter())    # 26
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())           # 81
sq.set_side(4)
print(sq.get_diagonal())       # ~5.66
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8

    