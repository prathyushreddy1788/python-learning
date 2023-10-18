import math

class Circle:
    """
        A class used to evaluate a circle
    """
    def __init__(self, r: float):
        self.radius = r
        self.area = self.calculate_area()

    def calculate_area(self) -> float:
        area = math.pi * math.pow(self.radius, 2)
        return area


class Square:
    ''' this class is used for calculating area of square'''

    def __init__(self, s: float):
        self.side = s
        self.area = self.calculate_area()
    def calculate_area(self) -> float:
        area = self.side*self.side
        return area



class Rectangle:
    ''' this class is used for evaluating area of a rectangle'''
    def __init__(self, l: float, b: float):
        self.length = l
        self.breadth = b
        self.area = self.calculate_area()
    def calcuate_area(self)-> float:
        area = self.length * self.breadth
        return area

class Triangle:
    ''' this class is used for calculation of area of triangle'''
    def __init__(self, b: float, h: float):
        self.base = b
        self.height = h
        self.area = self.calculate_area()

    def calcuate_area(self) -> float:
        area = 0.5*self.base * self.height
        return area

class VolumeOfSphere:

    '''this class is used for calculating volume of sphere'''
    def __init__(self, r: float):
        self.radius = r
        self.volume = self.calculate_volume()
    def calculate_volume(self):
        volume = 4/3 * math.pi * math.pow(self.radius, 3)
        return volume


volume1 = VolumeOfSphere(10.0)
print(volume1.volume)
