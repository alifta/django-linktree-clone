from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile, Link


# Create your views here.
class LinkListView(ListView):
    model = Link
