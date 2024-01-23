from django.urls import path

from .views import CategoryPostListView, HomeView, PostDetailView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),   
    path("category/<slug:slug>/", CategoryPostListView.as_view(), name='category'),   
    path("posts/<slug:slug>/", PostDetailView.as_view(), name='post-detail'),   
]
