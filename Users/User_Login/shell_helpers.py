from apps.user_login.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# use this function to create users with validations
def create_valid_user():

    user = {}
    print "Enter a First Name"
    user['first_name'] = raw_input()

    print "Enter a Last Name"
    user['last_name'] = raw_input()

    print "Enter an Email Address"
    user['email'] = raw_input()

    print "Enter an Age"
    user['age'] = raw_input()

    # we can pass user dictionary as keyword arguments (kwargs) like so
    # this will convert each key to a separate argument in the is_valid function
    # for example, {'first_name':'Michael'} will become -> is_valid(first_name='Michael')
    if is_valid(**user):
        User.objects.create(**user)
        print "successfully created a user"

def is_valid(**kwargs):
    valid = True
    # check db for existing email, this query will return a List, so we can check its length
    existing = User.objects.filter(email=kwargs['email'])
    if len(existing) > 0:
        valid = False
        print "Email is already in use"
    if len(kwargs['first_name']) < 3 or len(kwargs['last_name']) < 3:
        valid = False
        print 'Name fields must be at least 3 characters'

    # using django's built in email validator
    try:
        validate_email(kwargs['email'])
    except ValidationError:
        valid = False
        print "invalid email"

    return valid
