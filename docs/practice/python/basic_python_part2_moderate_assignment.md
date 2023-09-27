# Python Assignment - Moderate Questions

---

### 1. Function Basics
Write a Python function that takes two numbers as input and returns their sum. Then, call this function and print the result.

def sum(a:int,b:int):
    result = a+b
    return(result)
sum(1,2)
print(sum(1,2))

### 2. Exception Handling
Create a program that asks the user for input and handles a ValueError if the input cannot be converted to an integer. Provide an appropriate error message.

try:
    user_input: str = input("Please enter an integer: ")
    user_input: int = int(user_input)
    print("You entered:", user_input)
except ValueError:
    print("Error: Input is not a valid integer.")


### 3. File Reading
Write a Python program that reads a text file ("sample.txt") line by line and prints each line.


file_name = "samplex.txt"

try:
    
    with open(file_name, 'r') as file:
       
        for line in file:
            print(line.strip()) 

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


        
### 4. List Comprehensions
Given a list of numbers, use a list comprehension to create a new list containing only the even numbers.

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in original_list if num % 2 == 0]

print(even_numbers)


### 5. Debugging
Debug and correct it, explaining the errors you find.

def calculate_sum(a, b):
    result = a + b
    return result

x = 5
y = 7
print(calculate_sum(x, y))




### 6. Module Import
Create a Python module with a function that calculates the factorial of a number. Import this module into your main program and use the function to find the factorial of a given number.

def factorial(n:int):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
result = factorial(5)
print("Factorial:", result)


### 7. File Writing
Write a Python program that asks the user to enter their name and then saves it to a file called "names.txt."

user_name = input("Please enter your name: ")
with open("names.txt", "a") as file:
    file.write(user_name + "\n")

print("Your name has been saved to 'names.txt'.")


### 8. Error Handling with File I/O
Modify the file reading program from question 3 to handle the case where the file doesn't exist, displaying an error message.

try:

    user_name = input("Please enter your name: ")


    with open("names.txt", "a") as file:
        file.write(user_name + "\n")

    print("Your name has been saved to 'names.txt'.")
except FileNotFoundError:
    print("Error: The 'names.txt' file does not exist. Please create the file or check the file path.")
except Exception as e:
    print("An error occurred:", e)

    
### 9. Function with Default Arguments
Create a function that takes two arguments, one required and one optional. The optional argument should have a default value. Demonstrate calling this function both with and without providing the optional argument.

---

## Submission Guidelines
- Complete the code for each question in separate Python files (e.g., `question1.py`, `question2.py`, etc.).
- Provide comments and explanations where necessary to make your code understandable.

