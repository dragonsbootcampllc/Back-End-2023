class ShoppingCart:
    def __init__(self):
        self.items = []   #initialize an empty list to hold the items in the cart

    #add an item to the cart takes an item name and price as parameters 
    #and creates a dictionary representing the item.
    #This dictionary is appended to the items
    def add_item(self, item_name, item_price):
        item = {"name": item_name, "price": item_price}
        self.items.append(item)

    #finds the item with the specified name, and removes it from the list using the remove method
    def remove_item(self, item_name):
        for item in self.items:
            if item["name"] == item_name:
                self.items.remove(item)
                break

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item["price"]
        return total_price

# Example usage:
cart = ShoppingCart()

# Adding items to the cart
cart.add_item("twix", 0.5)
cart.add_item("twix", 0.5)
cart.add_item("snickers", 0.3)
cart.add_item("toffee", 0.4)
# Removing an item from the cart
cart.remove_item("snickers")

# Calculating the total price
total_price = cart.calculate_total_price()
print(f"Total Price: ${total_price}")