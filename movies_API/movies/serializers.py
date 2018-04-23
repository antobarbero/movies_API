from rest_framework import serializers

from .models import Movie, Person
from .utils import write_roman


class PersonInLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['pk', 'first_name', 'last_name', 'aliases']


class MovieSerializer(serializers.ModelSerializer):
    casting = PersonInLineSerializer(read_only=True, many=True)
    directors = PersonInLineSerializer(read_only=True, many=True)
    producers = PersonInLineSerializer(read_only=True, many=True)
    roman_release_year = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_roman_release_year(self, obj):
        return write_roman(obj.release_year)


class PersonSerializer(serializers.ModelSerializer):

    movies_as_actor = MovieSerializer(read_only=True, many=True)
    movies_as_director = MovieSerializer(read_only=True, many=True)
    movies_as_producer = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Person
        fields = '__all__'
