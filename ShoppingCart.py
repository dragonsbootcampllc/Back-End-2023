class Product:  
  def __init__(self, id, name, description, price):
    self.id = id
    self.name = name
    self.description = description
    self.price = price  


class Cart:
  # Products or Items in the cart
  # Item is an array of dictionaries, each dictionary representing item object and its quantity
  items = []
  
  def addItem(self, item: Product, quantity: int):
    # if item is already in the cart and wants to add more units of it
    if (self.items):
      for i in range(0, len(self.items)):
        if self.items[i]["item"].id == item.id:
          self.items[i]["quantity"] += quantity
          return
    
    self.items.append({"item" : item, 'quantity' : quantity})
    
  # Deletes the Item (All units of it) from the cart using its ID
  def removeItem(self, item_id):
    if (self.items):
      for item in self.items:
        if item["item"].id == item_id:
          self.items.remove(item)
  
  def getTotalPrice(self):
    totalPrice = 0
    if (self.items):
      for item in self.items:
        totalPrice += (item["item"].price * item["quantity"])
    return totalPrice;      

  # Deletes Units of an Item using its ID
  def removeUnits(self, item_id, numberOfUnits, removeAll = False):
    if (self.items):
      for item in self.items:
        if item["item"].id == item_id:
          if numberOfUnits < item["quantity"]:
            item["quantity"] -= numberOfUnits
          else:
            self.items.remove(item)


#MAIN METHOD
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
