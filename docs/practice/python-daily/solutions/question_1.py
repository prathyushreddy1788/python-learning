# 1. initialize smallest and second_smallest to float('inf')
def second_smallest_number(list_of_integers):
    smallest_number = float('inf')
    second_smallest = float('inf')
    # 2. get unique values in list using set
    set_of_numbers = set(list_of_integers)


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



    if second_smallest != float('inf'):
        print(f"{second_smallest} is the second_smallest number")




#
# 4 check if second smallest is float('inf')
# 4.1 if true print no second smallest number
# 4.2 otherwise print second smallest number


list_of_integers = [1,1,2]

second_smallest_number(list_of_integers)
