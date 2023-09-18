class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price, quantity):
        item = (item_name, price, quantity)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item[1] * item[2]
        return total_price
