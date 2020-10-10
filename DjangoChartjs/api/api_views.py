#filtering
from rest_framework import viewsets
from . import models
from . import serializers
from .filters import GamesFilter

class GamesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.GamesSerializer
    queryset = models.Games.objects.all()
    filter_class = GamesFilter


class OrganizationsViewset(viewsets.ModelViewSet):
    queryset = models.Organizations.objects.all()
    serializer_class = serializers.OrganizationsSerializer
    filter_fields = '__all__'

class PlayersViewset(viewsets.ModelViewSet):
    queryset = models.Players.objects.all()
    serializer_class = serializers.PlayersSerializer
    filter_fields = '__all__'

class TeamsViewset(viewsets.ModelViewSet):
    queryset = models.Teams.objects.all()
    serializer_class = serializers.TeamsSerializer
    filter_fields = '__all__'
