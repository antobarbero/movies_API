from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Movie, Person


class CastInline(admin.TabularInline):
    model = Person.movies_as_actor.through
    extra = 1
    verbose_name = _('Actor/Actress')
    verbose_name_plural = _('Casting')


class DirectorInline(admin.TabularInline):
    model = Person.movies_as_director.through
    extra = 1
    verbose_name = _('Director')
    verbose_name_plural = _('Directors')


class ProducerInline(admin.TabularInline):
    model = Person.movies_as_producer.through
    extra = 1
    verbose_name = _('Producer')
    verbose_name_plural = _('Producers')


class PersonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'aliases', ]
    list_display_links = ['pk', 'first_name', 'last_name', ]
    search_fields = ['pk', 'first_name', 'last_name', 'aliases', ]
    filter_horizontal = (
        'movies_as_actor', 'movies_as_director', 'movies_as_producer'
    )


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        CastInline,
        DirectorInline,
        ProducerInline,
    ]
    list_display = ['pk', 'title', 'release_year', ]
    list_display_links = ['pk', 'title', ]
    search_fields = ['pk', 'title', ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
