from django.conf.urls import include, url

from .views import PersonListAPIView, MovieListAPIView


app_name = 'movies'

urlpatterns = [
    # people
    url(r'^people/', include([
        url(
            r'^$',
            PersonListAPIView.as_view(),
            name='people-list'
        ),
    ])),

    # movies
    url(r'^movies/', include([
        url(
            r'^$',
            MovieListAPIView.as_view(),
            name='movie-list'
        ),
    ])),
]
