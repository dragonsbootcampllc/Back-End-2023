class item:
    def __init__(self, product, price, id):
        self.product = product
        self.price = float(price)
        self.id = id

    def Price(self):
        return self.price

    def Name(self):
        return self.product

    def Id(self):
        return self.id

    def show(self):
        print(
            f"Product Name : {self.product}\nId : {self.id}\nPrice : {self.price}")


class cart:
    items = {}
    itemsIds = []
    ids = 1
    totalSum = 0

    def _init_(self):
        pass

    def add(self, item):
        self.itemsIds.append(item.Id())
        self.items[item.Id()] = item
        self.totalSum += item.Price()
        print("Added successfully")
        print(f"Your product id is {self.ids}")
        self.ids += 1
    # It is best to remove using only the id of the item so we can apply binary search

    def search(self, itemId):
        found = 0
        l = -1
        index = 0
        r = len(self.itemsIds)
        while (l < r - 1):
            m = int((l + r) / 2)
            if (self.itemsIds[m] <= itemId):
                if (self.itemsIds[m] == itemId):
                    index = m
                    found = 1
                    break

                l = m
            else:
                r = m
        return (found, index)

    def remove(self, itemId):
        # we can reduce the complexity from O(len(list)) to O(log(len(list))) by storing only ids and
        # do binary search and make dictionary assign id to item data
        # but for now doing only for loop
        test = self.search(itemId)
        if (test[0]):
            print("Deleted successfully")
            self.itemsIds.remove(self.itemsIds[test[1]])
            del (self.items[itemId])
        else:
            print("Not found in the cart")

    def showProducts(self):
        print(f"\nProducts in cart\n")
        for i in range(len(self.itemsIds)):
            self.items[self.itemsIds[i]].show()
            print("-----------------------------------------")
    # current id for adding new id

    def getCurrentId(self):
        return self.ids

    def totalPrice(self):
        return self.totalSum


# simple tests
test = cart()
test.add(item("cc", 12, test.getCurrentId()))
test.add(item("cc", 12, test.getCurrentId()))
test.add(item("cc", 12, test.getCurrentId()))
test.add(item("cc", 12, test.getCurrentId()))
print(f"total Price is : {test.totalPrice()}")
test.showProducts()
test.remove(10)
test.showProducts()
test.add(item("cc", 12, test.getCurrentId()))
test.add(item("cc", 12, test.getCurrentId()))
test.add(item("cc", 12, test.getCurrentId()))
test.showProducts()
test.remove(5)
