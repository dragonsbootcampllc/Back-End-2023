class ShoppingCart:
    def __init__(self):
        self.items = {}  # Create an empty dictionary to store items in the cart

    def add_item(self, item_name, item_price, quantity=1):
        if item_name in self.items:
            # If the item already exists in the cart, update the quantity
            self.items[item_name]['quantity'] += quantity
        else:
            # If the item is not in the cart, add it with the specified quantity and price
            self.items[item_name] = {'quantity': quantity, 'price': item_price}
        return f"Added {quantity} {item_name}(s) to the cart."

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            # If the item exists in the cart, reduce its quantity
            self.items[item_name]['quantity'] -= quantity
            # Remove the item from the cart if the quantity becomes zero or negative
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]
            return f"Removed {quantity} {item_name}(s) from the cart."
        else:
            return f"{item_name} is not in the cart."

    def calculate_total(self):
        total = 0
        for item_name, item_data in self.items.items():
            total += item_data['price'] * item_data['quantity']
        return total

    def view_cart(self):
        if not self.items:
            return "Your cart is empty."
        cart_contents = "=== Shopping Cart ===\n"
        for item_name, item_data in self.items.items():
            cart_contents += f"{item_name} ({item_data['quantity']} x ${item_data['price']} each)\n"
        cart_contents += "====================="
        return cart_contents


def main():
    cart = ShoppingCart()
    while True:
        print("\nMenu:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity (default is 1): "))
            message = cart.add_item(item_name, item_price, quantity)
            print(message)
        elif choice == '2':
            item_name = input("Enter item name to remove: ")
            quantity = int(input("Enter quantity to remove (default is 1): "))
            message = cart.remove_item(item_name, quantity)
            print(message)
        elif choice == '3':
            cart_contents = cart.view_cart()
            print(cart_contents)
        elif choice == '4':
            total_price = cart.calculate_total()
            print(f"Total Price: ${total_price}")
            print("Thank you for shopping with us!")
            break
        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
