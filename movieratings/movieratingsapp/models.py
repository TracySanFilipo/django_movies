from django.db import models
from django.urls import reverse
from django.db.models import Count, Avg


class Movie(models.Model):
    title = models.CharField(max_length=160)

    def __repr__(self):
        return "{} {}".format(self.id, self.title)

    @property
    def get_url(self):
        return reverse('movie_detail', args=[self.pk])

    @property
    def rating_count(self):
        agg_qs = self.rating_set.all().aggregate(rating_count=Count('rating'))
        return agg_qs['rating_count']

    def avg_rating(self):
        avg = self.rating_set.all().aggregate(Avg('rating'))
        return round(avg['rating__avg'], 2)


class Rater(models.Model):
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    def __repr__(self):
        return "{} {} {} {}".format(self.age, self.gender, self.occupation, self.zip_code)

    @property
    def get_url(self):
        return reverse('rater_detail', args=[self.pk])


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=0)
    timestamp = models.CharField(max_length=32)

    def __repr__(self):
        return "{} {} {} {}".format(self.rater, self.movie, self.rating, self.timestamp)
