# Dunder Methods and Dunder Variables in Python

In Python, names that begin and end with double underscores, such as __init__ and __name__, are commonly referred to as dunder methods and dunder variables, respectively. "Dunder" is short for "double underscore". These special names have specific meanings and are used for various purposes in Python classes and objects.

## Dunder Methods
Dunder methods, also known as magic methods or special methods, allow you to define how objects of your class behave with built-in Python functions and operators. Here are a few examples:

**1. __init__(self, ...)**
The constructor method is automatically called when a new instance of a class is created. It initializes the object's attributes.

```python

class MyClass:
    def __init__(self, value):
        self.value = value

```

**2. __str__(self)**
This method is called by the str() function and print() function to get the string representation of an object.

```python
class MyClass:
    def __str__(self):
        return "This is an instance of MyClass"
```

**3. __add__(self, other)**
Allows you to customize the behavior of the + operator for objects of a class.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

These are just a few examples of dunder methods. There are many more, each serving a specific purpose. They provide a way to define how objects of a class behave with Python's built-in functions and operators, making Python a highly customizable and expressive programming language.

## Dunder Variables
Dunder variables are special variables in Python that have specific meanings and uses. Here are a few examples:

**1. __name__**
Represents the name of the current Python module. It is set to '__main__' when the script is run standalone.

```python
if __name__ == "__main__":
    # Code here will only run if the script is executed, not when imported
```

**2. __doc__**
Accesses the docstring associated with a module, class, function, or method.

```python
def my_function():
    """This function does something."""
    pass

print(my_function.__doc__)  # Output: This function does something.
```

**3. __file__**
Contains the path to the Python script being executed.

```python
print(__file__)  # Output: Path to the current Python script
```

These are just a few examples of dunder variables in Python. They provide a way to interact with and understand various aspects of Python's runtime environment, making them a powerful tool for customization and introspection.

