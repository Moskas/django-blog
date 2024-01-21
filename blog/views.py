from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.
class TutorialListView(ListView):
    model = Post
    context_object_name = 'tutorial_list'
    template_name = 'tutorials/tutorial_list.html'


class TutorialDetailView(DetailView): 
    model = Post
    context_object_name = 'tutorial'
    template_name = 'tutorials/tutorial_detail.html'