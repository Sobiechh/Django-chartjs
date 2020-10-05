from rest_framework import viewsets
from . import models
from . import serializers

class GameViewset(viewsets.ModelViewSet):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GameSerializer

class GameViewset(viewsets.ModelViewSet):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GameSerializer

class GameViewset(viewsets.ModelViewSet):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GameSerializer

class GameViewset(viewsets.ModelViewSet):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GameSerializer
