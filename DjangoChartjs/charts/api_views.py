from rest_framework import viewsets
from . import models
from . import serializers

class GamesViewset(viewsets.ModelViewSet):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GamesSerializer

class OrganizationsViewset(viewsets.ModelViewSet):
    queryset = models.Organizations.objects.all()
    serializer_class = serializers.OrganizationsSerializer

class PlayersViewset(viewsets.ModelViewSet):
    queryset = models.Players.objects.all()
    serializer_class = serializers.PlayersSerializer

class TeamsViewset(viewsets.ModelViewSet):
    queryset = models.Teams.objects.all()
    serializer_class = serializers.TeamsSerializer