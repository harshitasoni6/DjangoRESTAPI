from django.shortcuts import render

# Create your views here.
from books.models import Book
from rest_framework import viewsets

from books.serializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
