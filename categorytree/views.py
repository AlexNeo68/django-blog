from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Rubric

def categorytree(request):
    return render(request, 'categorytree/index.html', {'rubrics': Rubric.objects.all()}) 

class RubricDetailView(DetailView):
    model = Rubric
