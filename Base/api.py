from rest_framework import viewsets, permissions, mixins, filters, generics, status
from rest_framework.response import Response

from .models import Book, AuthorInBook, Author
from .serializers import BookSerializer, AuthorInBookSerializer, AuthorSerializer, BookInUserLibrarySerializer
from django.db.models import Avg, F
import requests

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['openlibrary_key', 'title', 'summary', 'image', 'qualification_avg']

    def get_ordering(self):
        ordering = self.request.query_params.get('ordering', 'addition_date')
        if ordering == 'qualification':
            return ['-qualification_avg']
        return [ordering]

    def get_queryset(self):
        queryset = Book.objects.annotate(qualification_avg=Avg('review__qualification'))
        only_reviewed = self.request.query_params.get('only_reviewed')
        if only_reviewed == '1':
            queryset = queryset.filter(qualification_avg__isnull=False)
        return queryset

class AuthorInBookViewSet(viewsets.ModelViewSet):
    queryset = AuthorInBook.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorInBookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer

class BooksFromUserSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    def get_queryset(self):
        query_set = Book.objects.filter(review__user=self.request.user)
        return query_set
