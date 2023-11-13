def value_of_invesntory(products):
    total_inventory_value = 0
    for information_of_product in products:
        total_inventory_value += information_of_product["price"]*information_of_product["quantity"]
    return total_inventory_value

products = [ {"id": 1, "name": "Product1", "price": 10, "quantity": 5},
             {"id": 2, "name": "Product2", "price": 15, "quantity": 3},
             {"id": 3, "name": "Product3", "price": 8, "quantity": 7},
             {"id": 4, "name": "Product4", "price": 20, "quantity": 2} ]
print(value_of_invesntory(products))