from django.urls import include, path

from .views import RubricDetailView, categorytree

urlpatterns = [
    path("", categorytree),
    path("rubrics/<int:pk>/", RubricDetailView.as_view(), name='rubric-detail')
]