## Assignment: Python Basics
### 1. Variable Declaration

Write Python code to declare a variable named age and assign it the value 25.

           age=25

### 2.Arithmetic Operations

Calculate the result of the expression 12 * 5 + 8 / 2 and assign it to a variable named result.

result = 12 * 5 + 8 / 2

print(result)

### 3.Conditional Statements

Write a Python program that takes an integer input from the user and prints whether it's even or odd.

number=input("enter integer ")
if int(number)%2 ==0:
    print("it is an even number")
else:
    print("it is an odd number")

### 4.Looping with Lists

Given the list fruits = ["apple", "banana", "cherry"], use a for loop to print each fruit in the list on a new line.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


### 5.String Manipulation

Create a variable greeting and assign it the string "Hello, World!". Then, print the length of the greeting.

greeting= "hello world"
print(len(greeting))

## Assignment: Data Types and Structures
### 6.Tuple Creation

Create a tuple named colors with three colors of your choice. Attempt to change one of the colors in the tuple and explain the result.

items in tuples are immutable.

### 7.Dictionary Manipulation

Create a dictionary representing a book with keys "title", "author", and "year". Print out the author's name.

book_information={
    "title" : "harry potter",
    "author": "j.k rowling",
    "year" : 2023
}
print(book_information["author"])


### 8.Logical Operators

Write a Python program that checks if a user's age is between 18 and 65 (inclusive) and prints whether they are of working age.

age=input("enter age ")
if int(age)>=18 and int(age)<=65:
    print("person belongs to working age ")
else:
    print("person doesnot belong to working age")


### 9.User Input and Conversion

Prompt the user to enter a number as a string. Convert it to an integer, add 10 to it, and print the result.
number=input("enter a number ")
result=int(number)+10
print(result)


### 10.String Concatenation

Create two variables, first_name and last_name, with your first and last name, respectively. Combine them to form a full name and print it.

first_name = "prathyush"
last_name = "reddy"
full_name = first_name + " " + last_name
print(full_name)

