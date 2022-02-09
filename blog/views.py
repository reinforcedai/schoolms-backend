from django.shortcuts import render
from rest_framework import viewsets

from .models import Category, News, Newsletter
from .serializers import CategorySerializer, NewsSerializer, NewsletterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = 'slug'

class NewsletterViewSet(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()