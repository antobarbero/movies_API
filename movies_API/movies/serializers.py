from rest_framework import serializers

from .models import Movie, Person


class PersonInLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['pk', 'first_name', 'last_name', 'aliases']


class MovieSerializer(serializers.ModelSerializer):
    casting = PersonInLineSerializer(read_only=True, many=True)
    directors = PersonInLineSerializer(read_only=True, many=True)
    producers = PersonInLineSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):

    movies_as_actor = MovieSerializer(read_only=True, many=True)
    movies_as_director = MovieSerializer(read_only=True, many=True)
    movies_as_producer = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Person
        fields = '__all__'
