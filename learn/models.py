from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    link = models.URLField()


class Quiz(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video)


class QuizResponse(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    quiz = models.ForeignKey(Quiz)
    passed = models.BooleanField()


class Address(models.Model):
    address_1 = models.CharField()
    address_2 = models.CharField()
    city = models.CharField()
    state = models.CharField()
    zip_code = models.CharField()  # Zip codes may start with 0.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.ForeignKey(Address)
