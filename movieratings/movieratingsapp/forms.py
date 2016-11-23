from django import forms
from .models import Rater, Rating
from django.contrib.auth.models import User
from django.utils import timezone


class sign_up(forms.Form):
    sign_up = forms.CharField(label='sign_up', max_length=100)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class RaterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = Rater
        fields = ['age', 'gender', 'occupation', 'zip_code']


class RatingsForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields= ['movie', 'rating']
        exclude = ['rater', 'timestamp']
