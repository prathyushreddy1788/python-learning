def string_list(list_of_strings):
    alphabet = input("enter starting alphabet ")
    length = input("enter length of string ")

    list_of_output =[]
    for item in list_of_strings:

        if item[0] == alphabet and len(item) >=int(length):
            list_of_output.append(item)
    return list_of_output

list_of_strings =  ["Apple", "Banana", "pAnt", "Orange", "pArt","cAr"]
print(string_list(list_of_strings))

