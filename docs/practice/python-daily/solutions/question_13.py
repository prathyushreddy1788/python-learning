class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def name1(self):
        print(f"my name is {self.name}")

    def age1(self):
        print(f"my age is {self.age}")

    def grade1(self):
        print(f"my grade is {self.grade}")


student1 = Student("prathyush", 26, "c")
student1.name1()
student1.age1()
student1.grade1()