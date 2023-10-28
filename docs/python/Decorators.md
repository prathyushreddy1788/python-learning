# Decorators in Python

Decorators provide a way to modify the behavior of functions or classes in Python. They allow you to wrap another function, enhancing or modifying its behavior. Decorators are powerful and are widely used in Python for tasks like logging, memoization, access control, etc.

## Basic Syntax

A decorator is a function that takes another function as an argument and returns a new function that usually extends or modifies the behavior of the input function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
Output:
```output

Something is happening before the function is called.
Hello!
Something is happening after the function is called.

```
In the example above, @my_decorator is a decorator applied to the say_hello function.

## Use Cases

### Function Decorators
```python
def timing_decorator(func):
    import time
    
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(2)
    print("Function executed!")

slow_function()
```

Output:
```output
Function executed!
Time taken: 2.0 seconds
```

### Class Decorators

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Something is happening before the function is called.")
        self.func()
        print("Something is happening after the function is called.")

@MyDecorator
def say_hi():
    print("Hi!")

say_hi()
```
Output:
```output
Something is happening before the function is called.
Hi!
Something is happening after the function is called.
```

Decorators are a powerful and elegant tool in Python, allowing you to modify or extend the behavior of functions and classes without changing their source code.