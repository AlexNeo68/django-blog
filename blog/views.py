from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Классический дизайн блога'
        return context

class PostDetailView(DetailView):
    model = Post
    
    

class CategoryPostListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(slug=self.kwargs['slug'])
        return context
