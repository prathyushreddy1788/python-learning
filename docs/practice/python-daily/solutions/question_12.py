class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        result = self.x + self.y
        return result
    def subtract(self):
        result = self.x - self.y
        return result
    def multiply(self):
        result = self.x * self.y
        return result

    def division(self):
        result = self.x / self.y
        return result


operation = Calculator(10, 20)

print(operation.add())
print(operation.subtract())
print(operation.multiply())
print(operation.division())

