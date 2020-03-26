from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
  """User siginup view"""
  form_class = CustomUserCreationForm
  succes_url = reverse_lazy('login')
  template_name = 'signup.html'