from django.urls import path

from .views import HomeView, PostDetailView, category

urlpatterns = [
    path("", HomeView.as_view(), name='home'),   
    path("category/<slug:slug>/", category, name='category'),   
    path("posts/<slug:slug>/", PostDetailView.as_view(), name='post-detail'),   
]
