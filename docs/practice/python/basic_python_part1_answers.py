# Assignment: Python Basics

# Question 1
age = 25

# Question 2
result = 12 * 5 + 8 / 2 

# Question 3
user_input = int(input("Enter an integer: "))
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Question 4
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Question 5
greeting = "Hello, World!"
print(len(greeting))

# Assignment: Data Types and Structures

# Question 6
colors = ("red", "green", "blue")
# Attempting to change a tuple element (will result in an error)
# colors[0] = "orange"

# Question 7
book = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
print(book["author"])

# Question 8
user_age = int(input("Enter your age: "))
if 18 <= user_age <= 65:
    print("You are of working age.")
else:
    print("You are not of working age.")

# Question 9
user_input = input("Enter a number as a string: ")
converted_number = int(user_input) + 10
print("Result after adding 10:", converted_number)

# Question 10
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
