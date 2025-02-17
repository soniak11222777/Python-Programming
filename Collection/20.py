import math

class Stock:
    def __init__(self, symbol = "", name = "", previousClosingPrice = 1, currentPrice = 2):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getSymbol(self):
        return self.__symbol
    
    def getName(self):
        return self.__name

    def getpreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def setpreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def getcurrentPrice(self):
        return self.__currentPrice

    def setcurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        change= (self.__currentPrice - self.__previousClosingPrice ) / self.__previousClosingPrice
        return change

def main():
    stock1 = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print("The stock symbol is", stock1.getSymbol() , ", the name is", stock1.getName(), ",the previous closing price was", stock1.getpreviousClosingPrice() ,", the current price is", stock1.getcurrentPrice(),", and the price-change percentage is", round(stock1.getChangePercent(),4), "%.") 

main()
