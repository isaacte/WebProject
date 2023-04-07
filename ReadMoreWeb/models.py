from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(Author)
    theme = models.ForeignKey(Theme)
    def _unicode_(self):
        return self.name + " - " + self.author

class Author(models.Model):
    name = models.CharField(max_length = 50)
    def _unicode_(self):
        return self.name

class Review(models.Model):
    qualification = models.IntegerField()
    book = models.ForeignKey(Book)
    video = models.ForeignKey(VideoReview)
    user = models.ForeignKey(User)
    def _unicode_(self):
        return self.qualification

class Theme(models.Model):
    theme = models.CharField(max_length = 50)
    def _unicode_(self):
        return self.theme
# Create your models here.
