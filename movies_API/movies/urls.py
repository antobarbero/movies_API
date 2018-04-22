from django.conf.urls import include, url

from .views import (MovieCreateAPIView, MovieRetrieveAPIView,
                    MoviesListAPIView, MovieUpdateAPIView, PeopleListAPIView,
                    PersonCreateAPIView, PersonRetrieveAPIView,
                    PersonUpdateAPIView)

app_name = 'movies'


urlpatterns = [
    # people
    url(r'^people/', include([
        url(
            r'^$',
            PeopleListAPIView.as_view(),
            name='people-list'
        ),
        url(
            r'^create/$',
            PersonCreateAPIView.as_view(),
            name='person-create'
        ),
        url(
            r'^(?P<pk>\d+)/', include([
                url(
                    r'^$',
                    PersonRetrieveAPIView.as_view(),
                    name='person-detail'
                ),
                url(
                    r'^update/$',
                    PersonUpdateAPIView.as_view(),
                    name='person-update'
                ),
            ])
        ),
    ])),

    # movies
    url(r'^movies/', include([
        url(
            r'^$',
            MoviesListAPIView.as_view(),
            name='movies-list'
        ),
        url(
            r'^create/$',
            MovieCreateAPIView.as_view(),
            name='movie-create'
        ),
        url(
            r'^(?P<pk>\d+)/', include([
                url(
                    r'^$',
                    MovieRetrieveAPIView.as_view(),
                    name='movie-detail'
                ),
                url(
                    r'^update/$',
                    MovieUpdateAPIView.as_view(),
                    name='movie-update'
                ),
            ])
        ),
    ])),
]
