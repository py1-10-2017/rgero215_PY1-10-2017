class Bike(object):
    """docstring for Bike."""
    def __init__(self, price, max_speed, miles=0):
        super(Bike, self).__init__()
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print '''Price: ${}
Max_speed: {}
Total miles: {}mph
======================================='''.format(self.price, self.max_speed, self.miles)
        return self

    def ride(self, num):
        riding = 10
        self.miles += riding * num
        print "Riding {} times at {}mph".format(num, riding)
        return self

    def reverse(self, num):
        reversing = 5
        self.miles -= reversing * num
        if self.miles < 0:
            self.miles = 0
            print "Reversing {} times at {}mph".format(num, reversing)
        else:
            print "Reversing {} times at {}mph".format(num, reversing)
        return self

bike1 = Bike(150, '10mph')
bike2 = Bike(200, '15mph')
bike3 = Bike(250, '20mph')

bike1.ride(3).reverse(1).displayInfo()
bike2.ride(2).reverse(2).displayInfo()
bike3.reverse(3).displayInfo()
