from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Review, Author, Book
from ..login_registration.models import User

# Create your views here.
def books(request):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        context = {
            'recent': Review.objects.recent_and_not()[0],
            'more': Review.objects.recent_and_not()[1]
        }
        return render(request, 'books/index.html', context)

def add(request):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        context = {
            'authors': Author.objects.all()
        }
        return render(request, 'books/edit.html', context)

def create(request):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        errs = Review.objects.validate_review(request.POST)
        if errs:
            for e in errs:
                messages.error(request, e)
        else:
            book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id

        return redirect('/books/{}'.format(book_id))

def create_additional(request, book_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        the_book = Book.objects.get(id=book_id)
        new_book_data = {
            'title': the_book.title,
            'author': the_book.author.id,
            'rating': request.POST['rating'],
            'review': request.POST['review'],
            'new_author': ''
        }
        errs = Review.objects.validate_review(new_book_data)
        if errs:
            for e in errs:
                messages.error(request, e)
        else:
            Review.objects.create_review(new_book_data, request.session['user_id'])
        return redirect('/books/' + book_id)

def show(request, book_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        context = {
            'book': Book.objects.get(id=book_id)
        }
        return render(request, 'books/review.html', context)

def profile(request, user_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        user = User.objects.get(id=user_id)
        unique_ids = user.reviews_left.all().values('book').distinct()
        unique_books = []
        for book in unique_ids:
            unique_books.append(Book.objects.get(id=book['book']))

        context = {
            'user': user,
            'unique_book_reviews': unique_books
        }
        return render(request, 'books/profile.html', context)

def delete(request, review_id):
    if 'login' not in request.session or request.session['login'] == False:
        return redirect('/')
    else:
        book = Book.objects.get(reviews= review_id).id
        Review.objects.get(id=review_id).delete()
        return redirect('/books/'+ str(book))
