from django.shortcuts import render
from .models import Book
from django.views.generic.list import ListView
# Create your views here.

class BookList(ListView):
    template_name = 'home.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 80