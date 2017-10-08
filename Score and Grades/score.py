import random
def random_num():
    return random.randint(60, 100)

def score_grades():
    for n in range(0, 10):
        n = random_num()
        if n >= 60 and n <= 69:
            print "Score {}; Your grade is D".format(n)
        elif n >= 70 and n <= 79:
            print "Score {}; Your grade is C".format(n)
        elif n >= 80 and n <= 89:
            print "Score {}; Your grade is B".format(n)
        elif n >= 90 and n <= 100:
            print "Score {}; Your grade is A".format(n)

score_grades()
