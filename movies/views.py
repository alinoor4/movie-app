from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def details(requests, movieId):
    movie = get_object_or_404(Movie, pk=movieId)
    return render(requests, 'movies/details.html', {'movie': movie})
