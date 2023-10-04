def string_list(list_of_strings):
    list_of_output =[]
    for item in list_of_strings:
        for character in item:
            if character == "A" and len(item) >=3:
                list_of_output.append(item)
    return list_of_output

list_of_strings =  ["Apple", "Banana", "Ant", "Orange", "Art"]
print(string_list(list_of_strings))