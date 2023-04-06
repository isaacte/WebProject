from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(Author)
    theme = models.ForeignKey(Theme)
    def __unicode__(self):
        return self.name + " - " + self.author

class Author(models.Model):
    name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Valoration(models.Model):
    qualification = models.IntegerField()
    book = models.ForeignKey(Book)
    video = models.ForeignKey(VideoReview)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.qualification

class Theme(models.Model):
    theme = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.theme

class VideoReview(models.Model):
    url = models.CharField(max_length = 200)
