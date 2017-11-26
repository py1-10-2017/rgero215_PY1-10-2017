from __future__ import unicode_literals
from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
        NAME_REGEX = re.compile(r'^[A-Za-z ]+$')
        errors = []
        if not EMAIL_REGEX.match(data['email']):
            errors.append("Please enter a valid email")
        elif not re.match(NAME_REGEX, data['name']):
            errors.append("Name should contain only letters")
        elif not data['alias'].isalpha() :
            errors.append("Alias should contain only letters")
        elif len(data['password']) > 1 and len(data['password']) < 8:
            errors.append("Password should be more than 8 characters!")
        elif not PASS_REGEX.match(data['password']):
            errors.append("Password should have at least 1 uppercase letter and 1 numeric value")
        elif data['confirm_password'] != data['password']:
            errors.append("Password and Password Confirmation should match")
        if len(errors) > 0:
            return False, errors
        else:
            return True,


    def validate_login(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
        errors = []
        if not EMAIL_REGEX.match(data['email']):
            errors.append("Please enter a valid email")
        elif not PASS_REGEX.match(data['password']):
            errors.append("Password should have at least 1 uppercase letter and 1 numeric value")
        if len(errors) > 0:
            return False, errors
        else:
            return True,

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    reviews = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} {} {} {} {}>".format(self.name, self.alias, self.email, self.reviews, self.created_at)
