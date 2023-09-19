from Product import Product
from Cart import Cart

product1 = Product(1, "Dairy Milk Chocolate", "Dark Chocolate", 50)
product2 = Product(2, "Biscuit", "A nice Biscuit", 3)
product3 = Product(3, "Domti Sandwich", "A white cheese sandwich", 8)

cart = Cart()

cart.addItem(product1, 5) 
cart.addItem(product2, 3)
cart.addItem(product3, 4)  

cart.removeItem(3)

cart.removeUnits(1, 2)

print("Total Price: ",cart.getTotalPrice())
