from django.urls import path, include
from rest_framework import routers

from .serializers import ArticleViewSet, CategoryViewSet, SeoViewSet, ArticleCountViewSet

router = routers.DefaultRouter()
router.register(r'blog', ArticleViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'seo', SeoViewSet)
router.register(r'count', ArticleCountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
