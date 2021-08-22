from rest_framework import routers

from api.v1.views import FilmWorkViewSet

router = routers.SimpleRouter()

router.register(r'movies', FilmWorkViewSet, basename='film_work')

urlpatterns = router.urls
