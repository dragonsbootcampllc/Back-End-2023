import Product

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