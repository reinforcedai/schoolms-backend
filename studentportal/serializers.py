from rest_framework import serializers
from rest_framework import viewsets

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student', 'pin', 'nin']

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer
