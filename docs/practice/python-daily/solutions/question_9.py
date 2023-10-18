#algorithm
# we have remove all the special characters,spaces and convert the string into lower case
# we have to check if each element in the input strings is present among the list of alphabets.....
# if that element is not present in the list of alphabets we have to ignore it and print
# rest of the elements
#we have to converst both the strings into lower cases
#now we have two strings with no spaces,special characters,punctuations and all of them are in lower cases
#now we have to compare both the strings
#know the length of the string = n
# we have to iterate over the length of the string(for i in range(0:n)
#if 1st alphabet in string-1[n-i+1] is equal to last alphabet in string-2[n-1] continue to next iteration

# if
#else: print "not a palindrome number"

def check_palindrome(input_string):
    input_string = input_string.lower()
    new_string = ""
    for char in input_string:
        ascii_value = ord(char)
        if ascii_value in range(97,123):
            new_string += char
        else:
            continue

    i = 0
    n = len(new_string)
    while i <= n-1 and new_string[i] == new_string[n-i-1]:
        i+=1
    if i == n:
        print("it's a palindrome")
    else:
        print("print it's not a palindrome number")









input_string = "A man, a plan, a canal, Panama!"
check_palindrome(input_string)
    