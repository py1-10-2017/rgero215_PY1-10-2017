import random

def random_coin():
    random_num = random.randint(0,1)
    return random_num




def coin_tosses():
    head = 0
    tail = 0
    count = 0
    for n in range(1, 5001):
        result = random_coin()
        if result == 0:
            head += 1
            count += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(count, head, tail)
        else:
            tail += 1
            count += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(count, head, tail)

coin_tosses()
