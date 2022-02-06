from rest_framework import serializers, viewsets

from .models import Category, News, Newsletter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'

class NewsletterViewSet(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()