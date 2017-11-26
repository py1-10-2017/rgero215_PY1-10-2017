from __future__ import unicode_literals
from ..login_registration.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    def __repr__(self):
        return "<Author object: {} >".format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books')
    def __repr__(self):
        return "<Book object: {} {} >".format(self.title, self.author)

class ReviewManager(models.Manager):
    def validate_review(self, post_data):
        errors = []

        if len(post_data['title']) < 1 or len(post_data['review']) < 1:
            errors.append('Field are requied')
        if not 'author' in post_data and len(post_data['new_author']) < 3:
            errors.append('New author names must be 3 or more characters')
        if not int(post_data['rating']) > 0 or not int(post_data['rating']) <= 5:
            errors.append('Invalid rating')
        return errors

    def create_review(self, clean_data, user_id):
        #retrive or create author
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])
        #retrive or create book
        the_book = None
        if not Book.objects.filter(title=clean_data['title']):
            the_book = Book.objects.create(title=clean_data['title'], author=the_author)
        else:
            the_book = Book.objects.get(title=clean_data['title'])

        #return a Review object
        return self.create(
            review = clean_data['review'],
            rating = clean_data['rating'],
            book = the_book,
            reviewer = User.objects.get(id=user_id)
        )

    def recent_and_not(self):
        '''
    returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
    containing the rest
    '''
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    reviewer = models.ForeignKey(User, related_name="reviews_left")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()
    def __repr__(self):
        return "<Book: {}>".format(self.book.title)
