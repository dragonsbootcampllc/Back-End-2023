class invoices:

    def __init__(self, items):
        self.items = items

    def add_item(self, item, price):
        self.items[item] = price

    def delete_item(self, item):
        del self.items[item]

    def calcul_total(self):
        total = 0
        for x in self.items.values():
            total += x
        return total

invoice = invoices({"foul": 20, "milk": 60})

while True:
    for x, y in invoice.items.items():
        print("item: " + x + " price = " + str(y))
    Number = int(
        input(
            "\n1-to add item \n2-to delete item \n3-to end this loop and calcul-total  \n\nplease enter the number : "))
    if Number == 1:
        item = input("enter Item : ")
        price = int(input("enter Price : "))
        invoice.add_item(item, price)

    elif Number == 2:
        counter = 0
        arr = []
        for x in invoice.items.keys():
            counter = counter + 1
            print(str(counter) + "- " + x)
            arr.append(x)
        Number_Of_item = int(input("enter number of Item you want to delete : "))
        invoice.delete_item(arr[Number_Of_item - 1])

    elif Number == 3:
        print_invoice = invoice.calcul_total()
        print("the invoice is :" + str(print_invoice))
        break
