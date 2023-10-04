def country_and_name(list_of_information):

    output_dict = {}

    for information in list_of_information:

        if information["country"] in output_dict:

            output_dict[information["country"]].append(information["name"])
        else:
            output_dict[information["country"]] = [information["name"]]




    return output_dict




list_of_information = [ {"name": "Alice", "age": 30, "country": "USA"},
                        {"name": "Bob", "age": 25, "country": "Canada"},
                        {"name": "Charlie", "age": 35, "country": "USA"},
                        {"name": "David", "age": 40, "country": "Canada"}]


print(country_and_name(list_of_information))





