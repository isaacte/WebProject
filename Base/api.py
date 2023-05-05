from rest_framework import viewsets, permissions
from .models import Book, AuthorInBook, Author
from .serializers import BookSerializer, AuthorInBookSerializer, AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer

class AuthorInBookViewSet(viewsets.ModelViewSet):
    queryset = AuthorInBook.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorInBookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer