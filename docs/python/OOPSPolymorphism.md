# Polymorphism in Object-Oriented Programming

## 1. Method Overriding
Method overriding occurs when a derived class provides a specific implementation for a method that is already defined in its base class. This allows objects of different classes to be treated as objects of a common base class.

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

# Polymorphism in action
dog = Dog()
cat = Cat()

dog.sound()  # Output: Woof!
cat.sound()  # Output: Meow!

```

In this example, both Dog and Cat classes override the sound() method from the Animal class. When calling sound() on objects of different classes, polymorphism allows the correct version of the method to be called.

## 2. Operator Overloading
Operator overloading allows the same operator to have different meanings for different data types. In Python, you can define methods with special names to enable operator overloading.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Operator overloading in action
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2  # Calls __add__() method
print(f"Resultant Point: ({result.x}, {result.y})")  # Output: (4, 6)
```

In this example, the __add__() method is defined in the Point class, allowing the + operator to be used for adding two Point objects. This demonstrates polymorphism, where the same operator behaves differently based on the data types involved.

### Best Use Cases for Polymorphism:
**Method overriding** is used when you want to provide a specific implementation of a method in a derived class while keeping the method signature the same as the base class.

**Operator overloading** is useful when you want to define custom behavior for operators to work with user-defined objects.

Polymorphism enables flexibility and abstraction in object-oriented programming, allowing code to be written in a way that is more generic and extensible.