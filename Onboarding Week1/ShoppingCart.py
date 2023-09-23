class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def addProduct(self, newProduct):
        self.products.append(newProduct)
        self.total_price += newProduct.price

    def removeProduct(self, productName):
        for product in self.products:
            if product.name == productName:
                self.total_price -= product.price
                self.products.remove(product)

    def totalCost(self):
        return self.total_price