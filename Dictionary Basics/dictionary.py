my_dict = {
    "name": "Ramon Geronimo",
    "age": 33,
    "country of birth": "The Dominican Republic",
    "favorite language": "Python"
}

def info(dict):
    for key, value in dict.iteritems():
        print "My {} is {}".format(key, value)
info(my_dict)
