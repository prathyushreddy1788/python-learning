#using sort method arrage the list of numbers in the list in ascending order
# we have to divide the list into number of sublists
# if the difference between two consecutive numbers in the list is greater than 1, then we have to create a list at this point
# then we have to compare the length of the sublists that are generated.
# the longest sublist is the list containing longest consecutive subsequence

def longest_consecutive_subsequence(input_list):
    input_list.sort()
    my_set = set(input_list) # to get unique values
    unique_list = list(my_set) # the unique set into list
    old_list = []
    new_list = []
    n = len(unique_list)
    l = 0
    for i in range(0,n-1):
        if unique_list[i+1] - unique_list[i] != 1:
            new_list = unique_list[l:i+1]
            l = i+1
            if len(new_list) > len(old_list):
                old_list = new_list
                new_list = []


    return old_list



input_list =[4, 4, 2, 8, 5, 3, 9, 1]
print(longest_consecutive_subsequence(input_list))