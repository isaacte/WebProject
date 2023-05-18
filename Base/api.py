from rest_framework import viewsets, permissions, mixins, filters, generics
from rest_framework.response import Response

from .models import Book, AuthorInBook, Author
from .serializers import BookSerializer, AuthorInBookSerializer, AuthorSerializer
from django.db.models import Avg, F
import requests

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.annotate(qualification_avg=Avg('review__qualification'))
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['ISBN', 'title', 'publish_date', 'pages_number', 'summary', 'edition', 'language', 'addition_date', 'qualification_avg']
    ordering = ['addition_date']

    def get_ordering(self):
        ordering = self.request.query_params.get('ordering', 'addition_date')
        if ordering == 'qualification':
            return ['-qualification_avg']
        return [ordering]

class AuthorInBookViewSet(viewsets.ModelViewSet):
    queryset = AuthorInBook.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorInBookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer

class BooksFromUserSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    def get_queryset(self):
        query_set = Book.objects.filter(review__user=self.request.user)
        return query_set