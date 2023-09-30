# question1.py
def calculate_sum(a, b):
    result = a + b
    return result

x = 5
y = 7
print(calculate_sum(x, y))

# question2.py
try:
    user_input = input("Enter a number: ")
    num = int(user_input)
    print(f"Entered number: {num}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# question3.py
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# question4.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# question6.py (Factorial Module)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Main Program (question6_main.py)
import factorial_module

number = 5
result = factorial_module.factorial(number)
print(f"Factorial of {number} is {result}")


# question7.py
user_name = input("Enter your name: ")
with open("names.txt", "w") as file:
    file.write(user_name)


# question8.py
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'sample.txt' does not exist.")


# question9.py
def function_with_optional_arg(required_arg, optional_arg="default_value"):
    print(f"Required argument: {required_arg}")
    print(f"Optional argument: {optional_arg}")
 
# Call with both arguments
function_with_optional_arg("value1", "value2")

# Call with only the required argument
function_with_optional_arg("value1")
