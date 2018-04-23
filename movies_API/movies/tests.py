from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Movie, Person


class PersonListAPITestCase(APITestCase):
    """Test case for the person objects list and creation."""

    def setUp(self):
        self.url = reverse('movies_api:person-list')

    def test_get_people_list(self):
        """
        Ensure we can get the complete people list.
        """
        person_1 = Person(
            first_name='Emilia',
            last_name='Clarke',
            aliases='Emi'
        )
        person_2 = Person(
            first_name='Peter',
            last_name='Dinklage',
        )
        person_3 = Person(
            first_name='Thomas',
            last_name='McCarthy',
            aliases='Thom'
        )

        Person.objects.bulk_create([person_1, person_2, person_3])

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), Person.objects.count())


class PersonCreationAPITestCase(APITestCase):
    """Test case for the person creation."""

    def setUp(self):
        self.url = reverse('movies_api:person-list')

    def test_create_person(self):
        """
        Ensure we can create a new person object.
        """
        user = User.objects.create(username='test_user')
        user.set_password('test123')
        user.save()
        self.client.login(username='test_user', password='test123')

        data = {
            'first_name': 'Emilia',
            'last_name': 'Clarke',
            'aliases': 'Emi'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.first().first_name, 'Emilia')

    def test_create_person_not_authenticated(self):
        """
        Ensure that the creation of a new person object is not allowed for not
        authenticated users.
        """
        data = {
            'first_name': 'Emilia',
            'last_name': 'Clarke',
            'aliases': 'Emi'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PersonDetailAPITestCase(APITestCase):
    """Test case for the person detail and update."""

    def setUp(self):
        self.person = Person.objects.create(
            first_name='Peter',
            last_name='Dinklage',
        )
        self.url = reverse(
            'movies_api:person-detail', kwargs={'pk': self.person.pk}
        )

    def test_person_detail(self):
        """
        Ensure we can get a person object detail.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_complete_data_schema(self):
        """
        Ensure the data of the response is complete.
        """
        response = self.client.get(self.url)
        data = response.data
        self.assertIn('id', data)
        self.assertIn('first_name', data)
        self.assertIn('last_name', data)
        self.assertIn('aliases', data)
        self.assertIn('movies_as_actor', data)
        self.assertIn('movies_as_director', data)
        self.assertIn('movies_as_producer', data)

    def test_update_person(self):
        """
        Ensure we can update a person object.
        """
        user = User.objects.create(username='test_user')
        user.set_password('test123')
        user.save()
        self.client.login(username='test_user', password='test123')

        data = {'first_name': 'Daenerys'}
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.first().first_name, 'Daenerys')

    def test_update_person_not_authenticated(self):
        """
        Ensure that the update of a person object is not allowed for not
        authenticated users.
        """

        data = {'first_name': 'Daenerys'}
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MoviesListAPITestCase(APITestCase):
    """Test case for the movies list and creation."""

    def setUp(self):
        self.url = reverse('movies_api:movie-list')

    def test_get_movies_list(self):
        """
        Ensure we can get the complete movies list.
        """
        movie_1 = Movie(
            title='The Mask',
            release_year=1994
        )
        movie_2 = Movie(
            title='Ace Ventura: Pet Detective',
            release_year='1994'
        )

        Movie.objects.bulk_create([movie_1, movie_2])

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), Movie.objects.count())

    def test_create_movie(self):
        """
        Ensure we can create a new movie object.
        """
        user = User.objects.create(username='test_user')
        user.set_password('test123')
        user.save()
        self.client.login(username='test_user', password='test123')

        data = {
            'title': 'The Mask',
            'release_year': 1994
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.first().title, 'The Mask')

    def test_create_movie_not_authenticated(self):
        """
        Ensure that the creation of a new movie object is not allowed for not
        authenticated users.
        """
        data = {
            'title': 'The Mask',
            'release_year': 1994
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MovieDetailAPITestCase(APITestCase):
    """Test case for the movie detail and update."""

    def setUp(self):
        self.movie = Movie.objects.create(
            title='The Mask',
            release_year=1994
        )
        self.url = reverse(
            'movies_api:movie-detail', kwargs={'pk': self.movie.pk}
        )

    def test_movie_detail(self):
        """
        Ensure we can get a movie object detail.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_complete_data_schema(self):
        """
        Ensure the data of the response is complete.
        """
        response = self.client.get(self.url)
        data = response.data
        self.assertIn('id', data)
        self.assertIn('title', data)
        self.assertIn('release_year', data)
        self.assertIn('casting', data)
        self.assertIn('directors', data)
        self.assertIn('producers', data)
        self.assertIn('roman_release_year', data)

    def test_update_movie(self):
        """
        Ensure we can update a movie object.
        """
        user = User.objects.create(username='test_user')
        user.set_password('test123')
        user.save()
        self.client.login(username='test_user', password='test123')

        data = {'title': 'The Mask 2'}
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.first().title, 'The Mask 2')

    def test_update_movie_not_authenticated(self):
        """
        Ensure that the update of a movie object is not allowed for not
        authenticated users.
        """
        data = {'title': 'The Mask 2'}
        response = self.client.patch(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
