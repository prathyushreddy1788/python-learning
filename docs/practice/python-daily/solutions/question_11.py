#ALGORITHM
#check if each alphabet in string-1 is present in string-2 and vice-versa
#if the above condition is true the print theay are anagram
#else print they are not anagrams
def remove_special_chars(input_str: str) -> str:
    """
    """
    output_string = ""
    for char in input_str:
        ascii_value = ord(char)
        if ascii_value in range(97,123):
            output_string += char
    return output_string

def check_anagram(input_string1,input_string2):
    input_string1 = input_string1.lower()
    input_string2 = input_string2.lower()
    new_string1 = remove_special_chars(input_string1)
    new_string2 = remove_special_chars(input_string2)
    # for char in input_string1:
    #     ascii_value = ord(char)
    #     if ascii_value in range(97,123):
    #         new_string1 += char

    # for char in input_string2:
    #     ascii_value = ord(char)
    #     if ascii_value in range(97,123):
    #         new_string2 += char

    if len(new_string1) == len(new_string2):
        for alpha in new_string1:
            if alpha in new_string2:
                pass
            else:
                print("not an anagram")
                break
        print("it is an anagram")
    else:
        print("not an anagram")



input_string1 = "listen"
input_string2 = "silent"
check_anagram(input_string1,input_string2)

# Time complexity: Big-O, Small-O
# Space complexity 