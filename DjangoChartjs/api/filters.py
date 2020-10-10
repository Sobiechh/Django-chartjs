import django_filters.rest_framework as filter
from . import models

class GamesFilter(filter.FilterSet):
    min_price = filter.NumberFilter(field_name = 'price', lookup_expr = 'gte')
    max_price = filter.NumberFilter(field_name = 'price', lookup_expr = 'lte')

    class Meta:
        model = models.Games
        filter_backends = (filter.DjangoFilterBackend,)
        fields = ('name', )