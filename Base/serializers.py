from rest_framework import serializers
from .models import Book, Author, AuthorInBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('ISBN', 'title', 'publish_date', 'pages_number', 'summary', 'edition', 'image', 'language')

class AuthorInBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInBook
        fields = ('book', 'author')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'biography', 'birth_date', 'decease_date', 'image')