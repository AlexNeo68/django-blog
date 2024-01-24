from pyexpat import model
from django.db.models import F
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
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

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


class TagPostListView(ListView):
    template_name = 'blog/tag.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        context["title"] = f'Посты по тегу: {tag.title}'
        return context

class SearchPostListView(ListView):
    template_name = 'blog/search_page.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('text_search'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_search"] = self.request.GET.get('text_search')
        context['search_param'] = f"&text_search={self.request.GET.get('text_search')}"
        context['title'] = "Поиск по постам"
        return context