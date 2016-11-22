from django.db import models
from django.urls import reverse
from django.db.models import Count, Avg
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, null=True)

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


def add_user():
    for r in Rater.objects.all():
        uid = "R"+str(r.id - 1)
        r.user = User.objects.create(username=uid, email="a@example.org", password="pass")
        r.user.set_password("pass")
        r.user.save()
        r.save()

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
#
# users = User.objects.all().select_related('profile')
