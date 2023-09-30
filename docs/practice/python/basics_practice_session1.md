# Programming Questions

## Question 1:
Write a Python program that does the following:
- Creates an empty list.
- Asks the user to enter five numbers, one at a time, and appends each number to the list.
- Calculates and prints the sum of the numbers in the list.

def sum():
""" this function calculates sum of numbers in a list"""
    total_sum: int = 0
    for num: str in my_list:
        total_sum += int(num)
    return total_sum

my_list = []
while True:
    item: str = input("Enter a number (or press Enter to finish): ")
    if item == "":
        break 
    my_list.append(item)
sum()
print(f"sum of all numbers is {sum()}")
  

## Question 2:
Create a Python dictionary representing a book with the following information:
- Title: "Python Programming"
- Author: "John Smith"
- ISBN: "978-1234567890"
- Year: 2022
Write a function that takes the dictionary as input and prints each key-value pair in a readable format.

def info_of_book(x):
    """this functions prints information about the book"""
    for key: str, value: str in my_dict.items():
        print(key, value)

my_dict = {
    "Title" : "Python Programming",
    "Author": "John Smith",
    "ISBN"  : "978-1234567890",
    "Year"  : "2022"
}

info_of_book(my_dict)





## Question 3:
Write a Python program that uses a `for` loop to print the first 10 even numbers (starting from 2) on separate lines.


for num: int in range(1,21):
    if num % 2 == 0:
        print(num)
    else:
        pass

## Question 4:
Write a Python function that checks if a given string is a palindrome. A palindrome is a word or phrase that reads the same backward as forward. For example, "racecar" and "madam" are palindromes.






## Question 5:
Create a Python module named "math_operations" that includes the following functions:
- `add(a, b)`: Adds two numbers and returns the result.
- `subtract(a, b)`: Subtracts the second number from the first and returns the result.
- `multiply(a, b)`: Multiplies two numbers and returns the result.
- `divide(a, b)`: Divides the first number by the second (non-zero) number and returns the result.
Write a separate Python script that imports the "math_operations" module and uses its functions to perform basic mathematical operations.


math_operations.py

def add(a: int, b: int):
"""this function is used for addition operation"""
    return a + b

def subtract(a: int, b: int):
"""this function is uded for subtraction operation"""
    return a - b

def multiply(a: int, b: int):
"""this function is used for multiplication operation"""
    return a * b

def divide(a: int, b: int):
"""this function is used for division operation"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


utils.py

import math_operations

result_add = math_operations.add(5, 3)
result_subtract = math_operations.subtract(10, 4)
result_multiply = math_operations.multiply(6, 7)
result_divide = math_operations.divide(8, 2)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
    




   
