class Product(object):
    """docstring for Product."""
    def __init__(self, price, item_name, weight, brand):
        super(Product, self).__init__()
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        self.tax = None


    def displayInfo(self):
        if self.tax == None:
            print '''Price: ${} + taxes
Item Name: {}
Weight: {}lb
Brand: {}
Status: {}
======================================='''.format(self.price, self.item_name, self.weight, self.brand, self.status)
        else:
            total = self.price * self.tax + self.price
            print '''Price: ${} + taxes {}
Total: ${}
Item Name: {}
Weight: {}lb
Brand: {}
Status: {}
======================================='''.format(self.price, self.tax, total, self.item_name, self.weight, self.brand, self.status)
        return self

    def sell(self):
        self.status = 'sold'
        return self

    def addTax(self,tax):
        tax = float(tax) / 100
        total = self.price + self.price * tax
        print '''Total price for the {} is ${}
========================================'''.format(self.item_name, total)
        self.tax = tax
        return  total

    def return_item(self,reason):
        if reason == 'defective':
            self.status = reason
            self.price = 0
            print ''' This itme has been returned as {}'''.format(reason)
        elif reason == 'like new' or reason == 'in the box':
            self.status = 'for sale'
            print ''' This itme has been return {}'''.format(reason)
        elif reason == 'opened':
            total = self.price - float(self.price) * 0.20
            self.status = 'used'
            self.price = total
            print ''' This itme has been return and the box has been {}'''.format(reason)
        return self

product1 = Product(200, 'iPad', 2, 'Apple').addTax(15)
product2 = Product(100, 'Head Phone', 1, 'Beats').return_item('opened').displayInfo()
product3 = Product(600, 'iPhone', 1, 'Apple').sell()
product4 = Product(250, 'HD Monitor', 25, 'Samsugn').return_item('like new').displayInfo()
product5 = Product(100, 'iPhone Case', 1, 'Mophie').return_item('defective').displayInfo()
