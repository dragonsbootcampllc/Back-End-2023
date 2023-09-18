class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price



class Cart:


    def __init__(self):
        self.items = []
        self.totalPrice = 0

    def addItem(self, newItem):
        self.items.append(newItem)
        self.totalPrice += newItem.price

    def removeItem(self, itemName):
        for item in self.items :
            if item.name == itemName :
                self.totalPrice = self.totalPrice - item.price
                self.items.remove(item)

    def totalCost(self):
        return self.totalPrice

newCart = Cart()

print("Filling the Cart##########################")
newItem = Item("t1", 5)
newCart.addItem(newItem)
newItem = Item("t2", 5)
newCart.addItem(newItem)
newItem = Item("t3", 5)
newCart.addItem(newItem)
newItem = Item("t4", 5)
newCart.addItem(newItem)
newItem = Item("t5", 5)
newCart.addItem(newItem)
print("Total cost : ")
print(newCart.totalCost())
def printNames(Cart):
    for item in newCart.items:
        print(item.name + '\n')
printNames(newCart)

print("after remove #############################")

newCart.removeItem('t2')
print("Total cost : ")
print(newCart.totalCost())
printNames(newCart)