from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Book

class BookListView(LoginRequiredMixin, ListView):
  """List view for the book object"""
  model = Book
  context_object_name = 'book_list'
  template_name = 'books/book_list.html'
  login_url = 'account_login'


class BookDetailView(
  LoginRequiredMixin,
  PermissionRequiredMixin,
  DetailView):
  """Detail view for the book object"""
  model = Book
  context_object_name = 'book'
  template_name = 'books/book_detail.html'
  login_url = 'account_login'
  permission_required = 'books.special_status'


class SearchResultsListView(ListView):
  """Search and list of books view"""
  model = Book
  context_object_name = 'book_list'
  template_name = 'books/search_results.html'

  def get_queryset(self): # new
    query = self.request.GET.get('q')
    return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))