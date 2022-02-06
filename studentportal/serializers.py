from rest_framework import serializers, viewsets, permissions

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student', 'pin',]

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
