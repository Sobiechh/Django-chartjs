from django.db.models import Sum, Avg
from pandas.tests.groupby import aggregate
from rest_framework import serializers

from . import models


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    #dynamic_data  = serializers.SerializerMethodField()
    class Meta:
        model = models.Games
        fields = '__all__'
    
    def to_representation(self, instance):
        original_representation = super().to_representation(instance)

        representation = {
            'aggregation': self.get_dynamic_data(instance),
            'detail': original_representation,
        }

        return representation
    
    def get_dynamic_data(self, obj):
        totalprice = models.Games.objects.all().aggregate(total_price=Sum('price'))
        avgprice = models.Games.objects.all().aggregate(avg_price=Avg('price'))
        return totalprice, avgprice

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
