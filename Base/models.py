from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from statistics import mean

# Create your models here.
class Author(models.Model):
    openlibrary_key = models.CharField(max_length=20, primary_key=True)
    name = models.TextField()
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    decease_date = models.DateField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class LiteraryGenre(models.Model):
    name = models.TextField(unique=True)

    @property
    def clean_name(self):
        return self.name.replace('/', '')

    def __str__(self):
        return self.name


class Book(models.Model):
    openlibrary_key = models.CharField(max_length=15, primary_key=True)
    title = models.TextField()
    summary = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


    @property
    def qualification(self):
        qualifications = self.review_set.values_list('qualification', flat=True)
        if qualifications:
            return mean(qualifications)
        return None

    def read_by_user(self, user):
        return BookInUserLibrary.objects.filter(book = self, user=user).exists()

class LiteraryGenreInBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    literary_genre = models.ForeignKey(LiteraryGenre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.literary_genre.name} -> {self.book.title}"

    class Meta:
        unique_together = ("book", "literary_genre")

class AuthorInBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.name} -> {self.book.title}"

    class Meta:
        unique_together = ("book", "author")

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    qualification = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.user} -> {self.book.title}"
    
    class Meta:
        unique_together = ("book", "user")

class BookInUserLibrary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} -> {self.user}"

    class Meta:
        unique_together = ("book", "user")