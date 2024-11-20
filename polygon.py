""""
Were gonna push the code to github 
Ali Alkhatib:
Om Singh: 
"""



# Task 1.1 to 1.3 creating a class and constructor 

class Polygon:
    def __init__(self,name,side):
        self.name = name
        self.side = side

# task 1.4

    def set_name(self,name):
        self.name = name
    def set_side(self,side):
        self.side = side
    def get_name(self):
        return self.name
    def get_side(self):
        return self.side
    
    def __eq__(self, other):
        if type(self) == type(other): 
            return self.name == other.get_name() and self.side == other.get_side()
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f"{self.get_name()} with sides: {self.get_side()}"
    
    def calculate_circumference(self):
        return sum(self.side)
    

def main():
    square = Polygon("Square",[3.0,3.0,3.0,3.0])
    triangle = Polygon("Triangle",[4.0,6.0,8.0])
    hexagon = Polygon("Hexagon",[2.0,3.0,4.0,6.0,7.0,8.0])

    # now we print each string and sum of sides
    print(square)
    print("The sum of sides is:",square.calculate_circumference())
    print(triangle)
    print("The sum of sides is:",triangle.calculate_circumference())
    print(hexagon)
    print("The sum of sides is:",hexagon.calculate_circumference())

if __name__ == "__main__":
    main()


