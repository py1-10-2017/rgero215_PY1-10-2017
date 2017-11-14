from apps.dojo_ninjas.models import *
from apps.books_authors.models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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

def create_book():
    book = {}
    print 'Enter name'
    book['name'] = raw_input()

    print 'Enter Description'
    book['desc'] = raw_input()

    if valid_book(**book):
        Book.objects.create(**book)
        print 'successfully created a book'

def create_author():
    author = {}
    print 'Enter First Name'
    author['first_name'] = raw_input()

    print 'Enter Last Name'
    author['last_name'] = raw_input()

    print 'Enter an Email'
    author['email'] = raw_input()

    if valid_author(**author):
        Author.objects.create(**author)
        print "successfully created a author"

def assign_book():
    for book in Book.objects.all():
        print '''Name: {} ID: {}'''.format(book.name, book.id)
    print 'Enter book id to assign to an author'
    id = raw_input()
    this_book = Book.objects.get(id=id)

    for author in Author.objects.all():
        print '''Name: {} ID: {}'''.format(author.first_name, author.id)
    print 'Enter author id to assign a book'
    author_id = raw_input()
    this_author = Author.objects.get(id=author_id)

    this_author.books.add(this_book)
    print "successfully assign {} to author {}".format(this_book.name, this_author.first_name)

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

def valid_book(**kwargs):
    valid = True
    if len(kwargs['name']) < 3:
        valid = False
        print 'The name of the book must be at least 3 characters'

    return valid

def valid_author(**kwargs):
    valid = True
    # check db for existing email, this query will return a List, so we can check its length
    existing = Author.objects.filter(email=kwargs['email'])
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
