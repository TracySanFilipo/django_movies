from django.shortcuts import render
from movieratingsapp import models
from .models import Movie, Rater, Rating
from django.http import HttpResponse
from django.db.models import Count, Avg
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .forms import UserForm

def index(request):
    return render(request, 'index.html')


def movie_detail(request, var):
    movie = models.Movie.objects.get(pk=var)
    all_ratings = movie.rating_set.order_by("rating")
    return render(request, 'movie_detail.html', {'movie':movie, 'all_ratings':all_ratings})


def movie_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_list.html', {'movies':movies})


def rater_detail(request, var):
    rater = models.Rater.objects.get(pk=var)
    all_user_ratings = rater.rating_set.order_by("rating")
    return render(request, 'rater_detail.html', {'rater':rater, 'all_user_ratings':all_user_ratings})


def rater_list(request):
    raters = models.Rater.objects.all()
    return render(request, 'rater_list.html', {'raters':raters})


def top_20(request):
    top_movies = models.Movie.objects.annotate(avg_rating=Avg('rating__rating')).order_by('-avg_rating')[:20]
    return render(request, 'top_movies.html', {'top_movies':top_movies})

#
# @login_required(login_url="login/")
# def rater_profile(request):
#     return render(request, "rater_profile.html")
#
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return redirct('rater_profile')
#         else:
#             return redirct('invalid_login')
#     else:
#         return redirect('invalid_login')
