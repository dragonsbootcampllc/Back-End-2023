# Dragons Bootcamp - Task 1
# Author: Abdallah Hussein Ibrahim
# Date: September  2023
# Program: ShoppingCart Class

import sys


class ShoppingCart:
    def __init__(self):
        self.items = {}  # dict of items
        # each item has (both) a price and a quantity >>> then use nested dict

    def addItem(self, itemName, price, quantity):
        if not isinstance(itemName, str) or not isinstance(price, (int, float)) or not isinstance(quantity, int):
            print("Invalid input types")
            sys.exit(1)
        if price <= 0 or quantity <= 0:
            print("Quantity and price must be greater than zero")
            sys.exit(1)
        # We may have two types of apples: one at $2 (lower quality) and another at $3 (good quality)
        # Generate a unique identifier like a primary key for the item based on name and price
        # to handle the case of same item with different prices
        # The format() method formats the specified value(s) and insert them inside the string's placeholder{}.
        # without changing the type of the variable inside it. unlike str(s)
        strPrice = "{}".format(int(price))
        itemID = itemName+"_"+strPrice
        if itemID not in self.items:
            self.items[itemID] = {"name": itemName,
                                  "price": price, "quantity": quantity}
        else:
            self.items[itemID]["quantity"] += quantity

    def totalPrice(self):
        total = 0
        nItems = 0
        print(f"Your Card has {len(self.items)} items.")
        for item in self.items:
            nItems += 1
            price = self.items[item]["price"]
            quantity = self.items[item]["quantity"]
            name = self.items[item]["name"]
            total += price * quantity
            print(
                f"Item Number {nItems}: {name} with a price of {price}$ per unit with quantity {quantity}. The total price of this item is {price * quantity}$")
        print(f"Total Price: {total}$")

    def reduceQuantity(self, itemName, price, quantity):
        strPrice = "{}".format(int(price))
        itemID = itemName+"_"+strPrice
        if itemID not in self.items:
            print("INVALID item name or price!")
            sys.exit(1)
        else:
            if (self.items[itemID]["quantity"] >= quantity and quantity > 0):
                self.items[itemID]["quantity"] -= quantity
                if (self.items[itemID]["quantity"] == 0):
                    quantityDeleted = self.items.pop(itemID)
                    print(
                        f"The item '{quantityDeleted['name']}' with a price of {quantityDeleted['price']}$ per unit has been removed from your shopping card.")
                else:
                    print(
                        f"The remaining quantity of '{self.items[itemID]['name']}' with a price of {self.items[itemID]['price']}$ per unit is {self.items[itemID]['quantity']}")
            else:
                print("INVALID quantity!")
                sys.exit(1)

    def removeItem(self, itemName, price):
        strPrice = "{}".format(int(price))
        itemID = itemName+"_"+strPrice
        if itemID not in self.items:
            print("INVALID item name or price!")
            sys.exit(1)
        else:
            quantityDeleted = self.items.pop(itemID)
            print(
                f"The item '{quantityDeleted['name']}' with a price of {quantityDeleted['price']}$ per unit has been removed from your shopping card.")

    def removeAllItems(self):
        self.items.clear()


c = ShoppingCart()
c.addItem("Apple", 2, 2)
c.addItem("Apple", 2, 2)
# Note that when we add 'Apple' with a different price in the line below, it will be treated as a distinct item, separate from the 'Apple' with a price of 2 dollars
c.addItem("Apple", 3, 2)

c.addItem("Egg", 4.75, 2)
c.addItem("milk", 30, 3)
# Reduce the quantity of a specific item from the shopping cart
c.reduceQuantity("Apple", 2, 2)
c.totalPrice()
# Remove a specific item from the shopping cart
c.removeItem("Apple", 2)
c.totalPrice()
# remove all items from the shopping cart
c.removeAllItems()
c.totalPrice()
