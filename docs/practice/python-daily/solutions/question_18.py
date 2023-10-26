#Design an OnlineShoppingCart class that represents a shopping cart for an online store.
# The class should have methods to add items, remove items, calculate the total price,
# and apply discounts. Each item can have attributes like name, price, and quantity.
# Implement methods to display the cart contents and the final invoice after applying discounts.
class Items:
    def __init__(self, name, price, quantity, discount):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.actual_price = price*quantity*(100-discount)/100


class ShoppingCart:

    def __init__(self):
        self.collection_items: list[Items] = []


    def add_items(self, items_obj : Items):
        self.collection_items.append(items_obj)


    def remove_items(self, items_obj : Items):
        self.collection_items.append(items_obj)


    def invoice(self):
        bill = 0
        for item in self.collection_items:
            print(f"{item.name} : {item.actual_price}")
            bill += item.actual_price

        print(f"total bill is {bill}")


item1 = Items("name", 30, 2, 50)
item2 = Items("biscuit", 100, 20, 40)
item3 = Items("apples", 50, 10, 50)

cart = ShoppingCart()
cart.add_items(item1)
cart.add_items(item2)
cart.add_items(item3)
cart.invoice()






