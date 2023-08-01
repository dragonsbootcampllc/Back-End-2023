#Stock trading application
class Stock:
    def __init__(self,symbol,name,price,quantity = 0):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.quantity = quantity
    def printStock(self):
        print(self.symbol," ",self.name,"",self.price," ",self.quantity," ")


class StockTradingApplication:
    def __init__(self):
      self.allStock= []
    def add_stock(self,symbol,name,price,):
       stock = Stock(symbol,name,price)
       self.allStock.append(stock)
    def buy_stock(self,stockName,quantity):
       for stock in self.allStock:
           if(stock.name==stockName):
                stock.price += 1
                stock.quantity += quantity

    def sell_stock(self,stockName,quantity):
       for stock in self.allStock:
           if(stock.name==stockName):
                stock.price -= 1
                if(stock.quantity-quantity >= 0):
                    stock.quantity -= quantity
                    return True
                else:
                    return False       
    def get_stocks(self):
        for stock in self.allStock:
            stock.printStock()

def main():
    stockApp = StockTradingApplication()
    stockApp.add_stock("Ban","Banana",5.5)
    stockApp.add_stock("wan","Watermelon",7.5)

    stockApp.buy_stock("Banana",50)
    stockApp.buy_stock("Watermelon",20)

    stockApp.sell_stock("Banana",10)
    stockApp.sell_stock("Watermelon",10)
    stockApp.get_stocks()

if __name__ == '__main__':
    main()
