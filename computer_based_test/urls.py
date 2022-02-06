from django.urls import path, include
from rest_framework import routers

from .serializers import MultiChoiceQuestionViewSet


router = routers.DefaultRouter()
router.register(r'cbt', MultiChoiceQuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
