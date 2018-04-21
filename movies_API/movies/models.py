from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

LOWEST_RELEASE_YEAR = 1800
HIGHEST_RELEASE_YEAR = 2999


class Person(models.Model):
    """
    Represents an instance of a person.
    """
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    aliases = models.CharField(
        _('aliases'),
        max_length=150,
        blank=True,
        null=True
    )
    movies_as_actor = models.ManyToManyField(
        'Movie',
        related_name='casting',
        blank=True
    )
    movies_as_director = models.ManyToManyField(
        'Movie',
        related_name='directors',
        blank=True
    )
    movies_as_producer = models.ManyToManyField(
        'Movie',
        related_name='producers',
        blank=True
    )


class Movie(models.Model):
    """Represents an instance of a movie."""
    title = models.CharField(_('title'), max_length=100)
    release_year = models.PositiveIntegerField(
        _('release_year'),
        validators=[
            MinValueValidator(LOWEST_RELEASE_YEAR),
            MaxValueValidator(HIGHEST_RELEASE_YEAR)
        ]
    )
