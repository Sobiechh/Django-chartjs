import django_filters.rest_framework as filter
from . import models

class GamesFilter(filter.FilterSet):
    min_price = filter.NumberFilter(field_name = 'price', lookup_expr = 'gte')
    max_price = filter.NumberFilter(field_name = 'price', lookup_expr = 'lte')
    start_date = filter.DateFilter(field_name='release_date', lookup_expr='gt') 
    end_date = filter.DateFilter(field_name='release_date', lookup_expr='lt')
    #date_range = filter.DateRangeFilter(field_name='release_date')

    class Meta:
        model = models.Games
        filter_backends = (filter.DjangoFilterBackend,)
        fields = ('name', )