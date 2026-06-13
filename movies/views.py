from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def details(requests, movieId):
    movie = Movie.objects.get(pk=movieId)
    return render(requests, 'movies/details.html', {'movie': movie})
