from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, PersonViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'people', PersonViewSet, base_name='person')
router.register(r'movies', MovieViewSet, base_name='movie')

app_name = 'movies_api'

urlpatterns = [
    url(
        r'^api/',
        include(router.urls),
    )
]
