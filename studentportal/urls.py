from django.urls import include, path
from rest_framework import routers
from .serializers import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
