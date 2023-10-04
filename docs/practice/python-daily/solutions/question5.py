def new_dict_inventory(store1,store2):
    new_stock = 0
    new_dict_items ={}
    for fruit,stock in store1.items():
        for fruit1,stock1 in store2.items():
            if fruit == fruit1:
                new_stock = stock + stock1
                new_dict_items[fruit] = new_stock
            elif fruit in new_dict_items.keys():
                new_dict_items[fruit] = stock
            elif fruit1 in new_dict_items.keys():
                new_dict_items[fruit1] = stock1



    return new_dict_items

store1 = {"apple": 10, "banana": 5, "orange": 8}
store2 = {"banana": 3, "orange": 6, "grapes": 12}
print(new_dict_inventory(store1,store2))