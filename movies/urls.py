from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='movieIndex'),
    path('<int:movieId>', views.details, name='movieDetails')
]
