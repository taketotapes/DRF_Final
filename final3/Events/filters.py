import django_filters
from .models import Event


class EventFilter(django_filters.FilterSet):
    min_date = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    max_date = django_filters.DateTimeFilter(field_name='date', lookup_expr='lte')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['min_date', 'max_date', 'location', 'category']


class EventFilterSearch(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['title', 'description']
