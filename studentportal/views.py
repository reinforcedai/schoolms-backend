from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]
