# 1. initialize smallest and second_smallest to float('inf')
def second_smallest_number(set_of_numbers):
    smallest_number = float('inf')
    second_smallest = 0
# 2. get unique values in list using set


# 3. check if the length of the set is greater than 2
    if len(set_of_numbers) >= 2:
        for current_number in set_of_numbers:
            if smallest_number > current_number:
                second_smallest = smallest_number
                smallest_number = current_number
            elif second_smallest > current_number:
                second_smallest = current_number
    else:
        print("there is no second smallest number")

# 3.1.if true => iterate through set:
#     2.1 compare current_number with smallest
#     2.1 if smallest is greater
#         2.2 set second_smallest to smallest
#         2.2 set smallest to current number
#     2.3 elif check if the second_smallest is greater than current_number
#         2.4 set the second smallest to current_number
# 3.2 otherwise print no second smallest number

    if second_smallest == float('inf'):
        print("there is no second smallest number")
    else:
        print(f"{second_smallest} is the second_smallest number")


#
# 4 check if second smallest is float('inf')
# 4.1 if true print no second smallest number
# 4.2 otherwise print second smallest number


list_of_integers = [2,3,5,6,7,9]
set_of_numbers = set(list_of_integers)
second_smallest_number(set_of_numbers)
