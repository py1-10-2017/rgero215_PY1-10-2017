class Car(object):
    """docstring for Car."""
    def __init__(self, price, speed, fuel, mileage):
        super(Car, self).__init__()
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        tax = 0
        if self.price > 10000:
            tax = float(0.15)
        else:
            tax = float(0.12)
        print '''Price: ${}
Speed: {}mph
Fuel: {}
Mileage: {}mpg
Tax: {}
======================================='''.format(self.price, self.speed, self.fuel, self.mileage, tax)
        return self


car1 = Car(2000, 35, 'Full', 15).display_all()
car2 = Car(2000, 5, 'Not Full', 105).display_all()
car3 = Car(2000, 15, 'Kind of Full', 95).display_all()
car4 = Car(2000, 25, 'Full', 25).display_all()
car5 = Car(2000, 45, 'Empty', 25).display_all()
car6 = Car(20000000, 35, 'Empty', 15).display_all()
