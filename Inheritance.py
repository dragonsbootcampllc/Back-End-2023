# Parent class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_details(self):
        print(f"Name: {self.name}, Price: {self.price}")

# Child classes
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    
    def get_details(self):
        super().get_details()
        print(f"Size: {self.size}")

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    
    def get_details(self):
        super().get_details()
        print(f"Brand: {self.brand}")

# Testing the subclasses
shirt = Clothing("T-Shirt", 20.99, "Medium")
shirt.get_details()         # Output: Name: T-Shirt, Price: 20.99, Size: Medium

phone = Electronics("iPhone", 999.99, "Apple")
phone.get_details()         # Output: Name: iPhone, Price: 999.99, Brand: Apple
