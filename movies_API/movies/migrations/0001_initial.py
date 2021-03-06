# Generated by Django 2.0.4 on 2018-04-21 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2999)], verbose_name='release year')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('aliases', models.CharField(blank=True, max_length=150, null=True, verbose_name='aliases')),
                ('movies_as_actor', models.ManyToManyField(blank=True, related_name='casting', to='movies.Movie')),
                ('movies_as_director', models.ManyToManyField(blank=True, related_name='directors', to='movies.Movie')),
                ('movies_as_producer', models.ManyToManyField(blank=True, related_name='producers', to='movies.Movie')),
            ],
        ),
    ]
