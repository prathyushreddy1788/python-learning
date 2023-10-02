# Question 1
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

# Question 2
def sum_of_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0)

# Question 3 
try:
    with open("words.txt", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"Word count: {word_count}")
except FileNotFoundError:
    print("The file 'words.txt' does not exist.")

# Question 4
import random
input("Press Enter to roll the dice...")
dice_roll = random.randint(1, 6)
print(f"You rolled a {dice_roll}")

# Question 5
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Question 6
def average_age(people):
    ages = [int(person["age"]) for person in people]
    return sum(ages) / len(ages)

# Question 7
def sort_strings(strings):
    return sorted(strings)

# Question 8
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
with open("user_info.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Age: {user_age}\n")

# Question 9
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return len([char for char in sentence if char in vowels])

# Question 10
number = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
