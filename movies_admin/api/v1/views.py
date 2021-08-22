from api.v1.filters import FilmWorkFilter
from api.v1.serializers import FilmWorkSerializer
from movies.models import FilmWork
from rest_framework import viewsets


class FilmWorkViewSet(viewsets.ModelViewSet):
    serializer_class = FilmWorkSerializer
    queryset = FilmWork.objects.all()
    filterset_class = FilmWorkFilter
