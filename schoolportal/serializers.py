from rest_framework import serializers, permissions, viewsets


from .models import School, SchoolAsset, StaffProfile, Calendar, AdmissionForm


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolViewSet(viewsets.ModelViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [permissions.IsAuthenticated]
