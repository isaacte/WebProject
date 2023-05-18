from rest_framework import serializers
from .models import Book, Author, AuthorInBook, BookInUserLibrary

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ('openlibrary_key', 'ISBN', 'title', 'publish_date', 'pages_number', 'summary', 'edition', 'image', 'language', 'authors', 'qualification', 'addition_date')
    
    def get_authors(self, obj):
        authors = []
        for author_in_book in AuthorInBook.objects.filter(book=obj):
            serializer = AuthorSerializer(author_in_book.author)
            authors.append(serializer.data)
        return authors


class AuthorInBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInBook
        fields = ('book', 'author')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('openlibrary_key', 'name', 'biography', 'birth_date', 'decease_date', 'image')

class BookInUserLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        field = BookInUserLibrary
        fields = ['book']