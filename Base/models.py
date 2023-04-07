from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    biography = models.TextField()
    birth_date = models.DateField()
    decease_date = models.DateField(blank=True, null=True)
    image = models.ImageField()

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class LiteraryGenre(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Language(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return f"{self.code - self.name}"

class Book(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=32)
    publish_date = models.DateField()
    pages_number = models.PositiveIntegerField()
    summary = models.TextField()
    edition = models.CharField(max_length=32)
    image = models.ImageField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class AuthorInBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"{self.book.title} - {self.author.name}"

class LiteraryGenreInBook(models.Model):
    literary_genre = models.ForeignKey(LiteraryGenre, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"{self.book.title} - {self.literary_genre.name}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    qualifications = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __unicode__(self):
        return f"{self.book.title} - {self.user}"