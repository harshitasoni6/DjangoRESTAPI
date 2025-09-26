from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from .models import Blog,Comment
from .serializers import BlogSerializer,CommentSerializer
# Create your views here.

from rest_framework.filters import SearchFilter,OrderingFilter
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_body']
    ordering_fields = ['id']

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

