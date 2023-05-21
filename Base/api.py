from rest_framework import viewsets, permissions, filters, generics, status

from .models import Book, AuthorInBook, Author
from .serializers import BookSerializer, AuthorInBookSerializer, AuthorSerializer
from django.db.models import Avg
import requests

class BookViewSet(generics.ListAPIView, viewsets.GenericViewSet):
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
        only_user_books = self.request.query_params.get('only_user_books')
        if only_reviewed == '1':
            queryset = queryset.filter(qualification_avg__isnull=False)
        if only_user_books == '1':
            queryset = queryset.filter(bookinuserlibrary__user=self.request.user)
        return queryset

class AuthorInBookViewSet(viewsets.ModelViewSet):
    queryset = AuthorInBook.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorInBookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer

class BooksFromUserSet(generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    def get_queryset(self):
        query_set = Book.objects.filter(review__user=self.request.user)
        return query_set
