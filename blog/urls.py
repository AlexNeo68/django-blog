from django.urls import path

from .views import category, index

urlpatterns = [
    path("", index, name='home'),   
    path("category/<str:slug>/", category, name='category'),   
]
