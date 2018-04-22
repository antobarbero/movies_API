from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class PeopleListAPIView(ListAPIView):
    """
    List all the Person objects.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveAPIView(RetrieveAPIView):
    """
    API view for Person detail.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonCreateAPIView(CreateAPIView):
    """
    API view for Person creation.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.all()


class PersonUpdateAPIView(UpdateAPIView):
    """
    API view for Person update.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.all()

    def get_queryset(self):
        return Person.objects.filter(pk=self.kwargs['pk'])


class MoviesListAPIView(ListAPIView):
    """
    List all the Movie objects.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieRetrieveAPIView(RetrieveAPIView):
    """
    API view for Movie detail.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieCreateAPIView(CreateAPIView):
    """
    API view for Movie creation.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()


class MovieUpdateAPIView(UpdateAPIView):
    """
    API view for Movie update.
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Movie.objects.all()
