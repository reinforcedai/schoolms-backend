from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import School, SchoolAsset, StaffProfile, Calendar, AdmissionForm
from .serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [permissions.IsAuthenticated]
