from django.shortcuts import render
from movieratingsapp import models
from .models import Movie, Rater, Rating
from django.http import HttpResponse
from django.db.models import Count, Avg


def index(request):
    return HttpResponse("Movie Rating for Older Movies")


def movie_detail(request, var):
    movie = models.Movie.objects.get(pk=var)
    return render(request, 'movie_detail.html', {'movie':movie})


def movie_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_list.html', {'movies':movies})


def rater_detail(request, var):
    rater = models.Rater.objects.get(pk=var)
    all_ratings = rater.rating_set.order_by("rating")
    return render(request, 'rater_detail.html', {'rater':rater, 'all_ratings': all_ratings})


def rater_list(request):
    raters = models.Rater.objects.all()
    return render(request, 'rater_list.html', {'raters':raters})


def top_20(request):
    top_movies = models.Movie.objects.annotate(avg_rating=Avg('rating__rating')).order_by('-avg_rating')[:20]
    return render(request, 'top_movies.html', {'top_movies':top_movies})
