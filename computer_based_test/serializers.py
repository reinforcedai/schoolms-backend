from rest_framework import serializers, viewsets, permissions

from .models import MultiChoiceQuestion


class MultiChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiChoiceQuestion
        fields = '__all__'

class MultiChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = MultiChoiceQuestion.objects.all()
    serializer_class = MultiChoiceQuestionSerializer
    # permission_classes = [permissions.IsAuthenticated]
