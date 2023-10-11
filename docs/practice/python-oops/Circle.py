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


