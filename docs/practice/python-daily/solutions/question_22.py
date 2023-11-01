class calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


    def add(self):

        result = self.a + self.b
        print(result)
    def sub(self):

        result = self.a - self.b
        print(result)

    def multiply(self):

        result = self.a * self.b
        print(result)

    def division(self):
        result = self.a/self.b
        print(result)


calculator(4,55).sub()