from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
        errors = []
        if not EMAIL_REGEX.match(data['email']):
            errors.append("Please enter a valid email")
        elif not data['first_name'].isalpha():
            errors.append("First name should contain only letters")
        elif not data['last_name'].isalpha() :
            errors.append("Last name should contain only letters")
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.created_at)
