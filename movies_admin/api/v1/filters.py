from django_filters import rest_framework as filters, DateTimeFromToRangeFilter

from movies.models import FilmWork


class FilmWorkFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    creation_date = DateTimeFromToRangeFilter(field_name='creation_date')

    class Meta:
        model = FilmWork
        fields = ['certificate', 'rating', 'type', 'mpaa_rating']
