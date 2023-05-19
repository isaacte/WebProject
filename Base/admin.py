from django.contrib import admin
from .models import Author, LiteraryGenre, Book, LiteraryGenreInBook, AuthorInBook, Review

# Register your models here.
admin.site.register(Author)
admin.site.register(LiteraryGenre)
admin.site.register(Book)
admin.site.register(LiteraryGenreInBook)
admin.site.register(AuthorInBook)
admin.site.register(Review)