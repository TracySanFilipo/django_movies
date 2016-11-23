from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/([0-9]+)', views.movie_detail, name='movie'),
    url(r'^movie_list$', views.movie_list, name='movie_list'),
    url(r'^rater/([0-9]+)', views.rater_detail, name='rater'),
    url(r'^rater_list$', views.rater_list, name='rater_list'),
    url(r'^top_movies$', views.top_20, name='top_movies'),
    url(r'^add_rating$', views.add_rating, name='add_rating'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^registration/$', views.register_user, name='register_user'),
    url(r'^topforuser/([0-9]+)', views.top_20_for_user, name='topforuser'),
]
