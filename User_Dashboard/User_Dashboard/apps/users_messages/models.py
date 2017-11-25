from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User
# Create your models here.

class Message(models.Model):
    user = models.ManyToManyField(User, related_name='messages')
    created_by = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Message object: {} {} {}>".format(self.created_by, self.message, self.created_at)

class Comment(models.Model):
    created_by = models.CharField(max_length=255)
    message = models.ManyToManyField(Message, related_name='comments')
    message_id = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Message object: {} {} {}>".format(self.created_by, self.comment, self.created_at)
