from django.shortcuts import render
from books.models import Book, Author, Tag

def home(request):
    books = Book.objects.all()
    return render(
        request=request,
        context={"books": books},
        template_name="books/home.html"
    )