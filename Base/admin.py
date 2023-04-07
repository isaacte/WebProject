from django.contrib import admin
from .models import Author, Publisher, LiteraryGenre, Book, LiteraryGenreInBook, AuthorInBook, Language, Review

# Register your models here.
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(LiteraryGenre)
admin.site.register(Book)
admin.site.register(LiteraryGenreInBook)
admin.site.register(AuthorInBook)
admin.site.register(Language)
admin.site.register(Review)