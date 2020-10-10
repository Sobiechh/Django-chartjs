from rest_framework import serializers
from . import models

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Games
        fields = '__all__'

class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = '__all__'
    
class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Players
        fields = '__all__'

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teams
        fields = '__all__'
