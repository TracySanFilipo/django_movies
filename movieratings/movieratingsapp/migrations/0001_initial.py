# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 18:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=2)),
                ('occupation', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('timestamp', models.CharField(max_length=32)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratingsapp.Movie')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratingsapp.Rater')),
            ],
        ),
    ]
