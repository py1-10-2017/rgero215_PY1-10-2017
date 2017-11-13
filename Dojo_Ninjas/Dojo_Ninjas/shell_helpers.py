from apps.dojo_ninjas.models import *

# use this function to create users with validations
def create_dojo():

    dojo = {}
    print "Enter Dojo's Name"
    dojo['name'] = raw_input()

    print "Enter Dojo's City"
    dojo['city'] = raw_input()

    print "Enter Dojo's State"
    dojo['state'] = raw_input()

    print "Enter Dojo's Description"
    dojo['desc'] = raw_input()

    if is_valid(**dojo):
        Dojo.objects.create(**dojo)
        print "successfully created a dojo"

def create_ninja():
    ninja = {}
    print 'Enter First Name'
    ninja['first_name'] = raw_input()

    print 'Enter Last Name'
    ninja['last_name'] = raw_input()

    print 'Enter Dojo ID: Mountain View ID: 1, Seattle ID: 2 and New York ID: 3'
    id = raw_input()
    this_dojo = Dojo.objects.get(id=id)
    ninja['dojo'] = this_dojo

    if valid_ninja(**ninja):
        Ninja.objects.create(**ninja)
        print 'successfully created a ninja'



def is_valid(**kwargs):
    valid = True
    existing = Dojo.objects.filter(name=kwargs['name'])
    if len(existing) > 0:
        valid = False
        print "Dojo is already created"
    if len(kwargs['name']) < 3 or len(kwargs['city']) < 3:
        valid = False
        print 'Name and City fields must be at least 3 characters'

    return valid

def valid_ninja(**kwargs):
    valid = True
    if len(kwargs['first_name']) < 3 or len(kwargs['last_name']) < 3:
        valid = False
        print 'First name and last name must be at least 3 characters'

    return valid
