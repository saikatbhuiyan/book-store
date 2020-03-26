from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
  """View for the home page"""
  template_name = 'home.html'


class AboutPageView(TemplateView):
  """View for the about page"""
  template_name = 'about.html'