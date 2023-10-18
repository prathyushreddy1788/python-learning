# Inheritance in Object-Oriented Programming

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass/derived class) to inherit properties and behaviors from an existing class (superclass/base class). This promotes code reusability and establishes a relationship between the classes.

# Types of Inheritance in Object-Oriented Programming
Inheritance in object-oriented programming can occur in several ways, leading to different types of inheritance. Each type serves a specific purpose and is used in different scenarios

## 1. Single Inheritance
Single inheritance involves a single base class and a single derived class. The derived class inherits the properties and behaviors of the base class.

```python 
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def display(self):
        print("Child class method")

# Creating objects
child_obj = Child()

# Accessing methods
child_obj.show()    # Output: Parent class method
child_obj.display() # Output: Child class method
```

**Best Place to Use:** Single inheritance is best suited when you want to inherit properties and behaviors from a single source.

## 2. Multiple Inheritance
Multiple inheritance involves a class inheriting properties and behaviors from more than one base class. Python supports multiple inheritance.

```python
class Class1:
    def method1(self):
        print("Method from Class1")

class Class2:
    def method2(self):
        print("Method from Class2")

class Derived(Class1, Class2):
    def display(self):
        print("Derived class method")

# Creating object
derived_obj = Derived()

# Accessing methods
derived_obj.method1() # Output: Method from Class1
derived_obj.method2() # Output: Method from Class2
derived_obj.display() # Output: Derived class method
```

**Best Place to Use:** Multiple inheritance is useful when a class needs to inherit properties and behaviors from multiple sources.

## 3. Multilevel Inheritance
Multilevel inheritance involves a chain of inheritance where a class serves as a base class for another class, creating a hierarchy of classes.

```python

class Grandparent:
    def method1(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def method2(self):
        print("Method from Parent")

class Child(Parent):
    def method3(self):
        print("Method from Child")

# Creating object
child_obj = Child()

# Accessing methods
child_obj.method1() # Output: Method from Grandparent
child_obj.method2() # Output: Method from Parent
child_obj.method3() # Output: Method from Child

```

**Best Place to Use:** Multilevel inheritance is appropriate when you have a hierarchy of classes where each class inherits properties and behaviors from its parent.

## 4. Hierarchical Inheritance
Hierarchical inheritance involves multiple derived classes inheriting from a single base class.

```python

class Base:
    def show(self):
        print("Base class method")

class Derived1(Base):
    def display1(self):
        print("Derived1 class method")

class Derived2(Base):
    def display2(self):
        print("Derived2 class method")

# Creating objects
derived1_obj = Derived1()
derived2_obj = Derived2()

# Accessing methods
derived1_obj.show()    # Output: Base class method
derived1_obj.display1() # Output: Derived1 class method

derived2_obj.show()    # Output: Base class method
derived2_obj.display2() # Output: Derived2 class method

```

**Best Place to Use:** Hierarchical inheritance is suitable when multiple classes share common properties and behaviors with a single base class.