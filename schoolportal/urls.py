from django.urls import include, path
from rest_framework import routers
from .serializers import SchoolViewSet


router = routers.DefaultRouter()
router.register(r'school', SchoolViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
