from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, NewsViewSet, NewsletterViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'newsletter', NewsletterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
