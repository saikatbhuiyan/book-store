from django.views.generic import ListView, DetailView

from .models import Book

class BookListView(ListView):
  """List view for the book object"""
  model = Book
  context_object_name = 'book_list'
  template_name = 'books/book_list.html'


class BookDetailView(DetailView):
  """Detail view for the book object"""
  model = Book
  context_object_name = 'book'
  template_name = 'books/book_detail.html'