class Animal(object):
    """docstring for Animal."""
    def __init__(self, name):
        self.name = name
        self.health = 100


    def walk(self, num):
        num *= 1
        self.health -= num
        return self

    def run(self, num):
        num *= 5
        self.health -= num
        return self

    def display_health(self):
        print '''The animal health is {}'''.format(self.health)
        return self

animal1 = Animal('Cat').walk(3).run(2).display_health()

class Dog(Animal):
    """docstring for Dog."""
    def __init__(self, health):
        self.health = 150


    def pet(self, num):
        num *= 5
        self.health += num
        return self

dog1 = Dog('Coco').walk(3).run(2).pet(1).display_health()

class Dragon(Animal):
    """docstring for Dragon."""
    def __init__(self, health):
        self.health = 170


    def fly(self, num):
        num *= 10
        self.health -= num
        return self

    def display_health(self):
        print 'I am a Dragon and my health is {}'.format(self.health)

dragon1 = Dragon('Elliot').fly(5).display_health()
