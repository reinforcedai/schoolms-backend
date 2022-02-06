from rest_framework import serializers, viewsets
from django.db.models import Count

from .models import Article, Category, Seo, ArticleCount

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seo
        fields = '__all__'

class SeoViewSet(viewsets.ModelViewSet):
    queryset = Seo.objects.all()
    serializer_class = SeoSerializer

class ArticleCountSerializer(serializers.ModelSerializer):
    article_count = serializers.ReadOnlyField(default=Article.objects.count())
    # article_count = serializers.PrimaryKeyRelatedField(queryset=Article.objects.count())
    class Meta:
        model = ArticleCount
        fields = ['article_count']

class ArticleCountViewSet(viewsets.ModelViewSet):
    queryset = ArticleCount.objects.all()
    serializer_class = ArticleCountSerializer
