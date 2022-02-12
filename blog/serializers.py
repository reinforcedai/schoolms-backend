from rest_framework import serializers

from .models import Category, News, Newsletter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['title', 'description', 'content', 'image', 'author', 'category', 'slug']
        lookup_field = 'slug'
    
class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'
