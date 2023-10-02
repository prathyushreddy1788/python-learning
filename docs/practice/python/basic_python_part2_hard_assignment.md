### Question 1
Write a Python program that calculates and prints the area of a rectangle. Prompt the user for the length and width of the rectangle as input.

l=input("enter length of rectangle ")
b = input("enter breadth of rectangle ")
l=int(l)
b=int(b)
A=l*b
print(f"area of rectangle is {A}")


### Question 2
Create a Python function that takes a list of numbers as input and returns the sum of all the odd numbers in the list.

def sum_odd():
    odd_sum = 0
    for num in my_list:
        if int(num)% 2 != 0:
            odd_sum += int(num)
    return odd_sum


my_list = []
while True:
    item = input("Enter an item (or press Enter to finish): ")
    if item == "":
        break  # Exit the loop if the user presses Enter without input
    my_list.append(item)
sum_odd()
print(f"sum of odd numbers is {sum_odd()}")


### Question 3
Write a Python program that reads a text file ("words.txt") and counts the number of words in the file. Display the word count.

# Open the file for reading
file_name = "samplex.txt"

try:
    with open(file_name, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

        # Split the contents into words using whitespace as a delimiter
        words = file_contents.split()

        # Count the number of words
        word_count = len(words)

        # Display the word count
        print(f"Number of words in {file_name}: {word_count}")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

### Question 4
Develop a Python program that simulates a simple dice rolling game. The program should generate a random number between 1 and 6 (inclusive) to simulate a dice roll when the user presses Enter.

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    dice_roll = roll_dice()
    print(f"You rolled a {dice_roll}")

    play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thanks for playing!")




### Question 5
Create a Python function that checks if a given number is prime or not. Prompt the user for a number and display whether it is prime or not. 



### Question 6
Write a Python program that reads a CSV file containing names and ages of people. Calculate and display the average age of the people in the file.



### Question 7
Implement a Python function that takes a list of strings as input and returns a new list containing the strings sorted in alphabetical order.

### Question 8
Create a Python program that prompts the user for their name and age. Write this information to a text file ("user_info.txt").

### Question 9
Write a Python function that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in the sentence. Display the vowel count.

### Question 10
Develop a Python program that uses a for loop to print the multiplication table of a given number. Prompt the user for the number.

