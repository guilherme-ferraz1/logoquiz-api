from rest_framework import viewsets
from questions.api import serializers
from questions import models

class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsSerializer
    queryset = models.Questions.objects.all()