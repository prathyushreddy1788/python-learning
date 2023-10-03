You are given a list of dictionaries, where each dictionary represents a product with attributes: "id", "name", "price", and "quantity". Write a Python function that takes this list as input and returns the total value of the inventory (sum of price * quantity for all products). Additionally, identify and print the name of the product with the highest price per unit.

For example:

products = [
    {"id": 1, "name": "Product1", "price": 10, "quantity": 5},
    {"id": 2, "name": "Product2", "price": 15, "quantity": 3},
    {"id": 3, "name": "Product3", "price": 8, "quantity": 7},
    {"id": 4, "name": "Product4", "price": 20, "quantity": 2}
]

The function should return the total inventory value (in this case, 10*5 + 15*3 + 8*7 + 20*2 = 199) and print the name of the product with the highest price per unit (in this case, "Product4"). 