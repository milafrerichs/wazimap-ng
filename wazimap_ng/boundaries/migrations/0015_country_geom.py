# Generated by Django 2.2.8 on 2020-01-21 14:44

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0014_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
    ]
