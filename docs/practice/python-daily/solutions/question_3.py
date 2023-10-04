def country_and_name(list_of_information):
    list_of_namesUSA = []
    list_of_namesCANADA = []
    output_dict = {}
    for information in list_of_information:
        for key, value in information.items():
            if key == "country" and value == "USA":
                list_of_namesUSA.append(information["name"])
            elif key == "country" and value == "Canada":
                list_of_namesCANADA.append(information["name"])
    output_dict["USA"] = list_of_namesUSA
    output_dict["Canada"] = list_of_namesCANADA
    return output_dict




list_of_information = [ {"name": "Alice", "age": 30, "country": "USA"},
                        {"name": "Bob", "age": 25, "country": "Canada"},
                        {"name": "Charlie", "age": 35, "country": "USA"},
                        {"name": "David", "age": 40, "country": "Canada"}]


print(country_and_name(list_of_information))





