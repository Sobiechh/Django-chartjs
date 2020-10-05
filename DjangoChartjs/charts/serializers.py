from rest_framework import serializers
from . import models

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Games
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organizations
        fields = '__all__'
    
class PlayerOrganization(serializers.ModelSerializer):
    class Meta:
        model = models.Players
        fields = '__all__'

class TeamOrganization(serializers.ModelSerializer):
    class Meta:
        model = models.Teams
        fields = '__all__'
