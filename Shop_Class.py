class Shop:
    shop_menu = {}
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.shop_menu[name] = self.quantity

    def addStock(self, addquantity):
        self.quantity += addquantity
        self.shop_menu[self.name] = self.quantity

    def reduceStock(self, reducequantity):
        if self.shop_menu[self.name] < reducequantity:
            #raise Exception ("Cannot remove more than stocked")
            print("You cannot remove more then you have")
        else:
            self.quantity -= reducequantity
            self.shop_menu[self.name] = self.quantity

    def setPrice(self, new_price):
        self.price = new_price

    def raisePrice(self, raiseprice):
        self.price += raiseprice

    def givePrice(self):
        return self.price

    def giveQuantity(self):
        return self.quantity

    def __str__(self):
        return "T-shirt {} for {}, we have {} pieces".format(self.name, self.price, self.quantity)