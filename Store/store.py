class Store(object):
    """docstring for Store."""
    def __init__(self, location, owner):
        super(Store, self).__init__()
        self.Product = []
        self.location = location
        self.owner = owner


    def inventory(self):
        count = 0
        for product in self.Product:
            count += 1
            print '''{}- {}: '''.format(count, product.item_name)
            print product.displayInfo()
        print '**************************************************'
        return self

    def add(self, Product):
        self.Product.append(Product)
        print '''{} has been succefully added to the inventory
=========================================='''.format(Product.item_name)
        return self


    def remove(self, item_name):
        try:
            for product in self.Product:
                if product.item_name == item_name:
                    self.Product.remove(product)
                    print "{} has been remove from the inventory".format(product.item_name)
        except ValueError:
            print "{} is not in the inventory".format(Product)
        return self

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

        print '''Price: ${} + taxes
Item Name: {}
Weight: {}lb
Brand: {}
Status: {}
======================================='''.format(self.price, self.item_name, self.weight, self.brand, self.status)
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

product1 = Product(200, 'iPad', 2, 'Apple')
product2 = Product(100, 'Head Phone', 1, 'Beats')
product3 = Product(600, 'iPhone', 1, 'Apple')
product4 = Product(250, 'HD Monitor', 25, 'Samsugn')
product5 = Product(100, 'iPhone Case', 1, 'Mophie')




store1 = Store( 'Santiago', 'Ramon Geronimo')
store1.add(product1)
store1.add(product2)
store1.add(product3)
store1.add(product4)
store1.add(product5)
store1.inventory()
store1.remove('iPad').inventory()
