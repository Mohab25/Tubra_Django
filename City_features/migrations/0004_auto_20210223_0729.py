# Generated by Django 3.1 on 2021-02-23 07:29

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('City_features', '0003_city_blocks_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_blocks',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
    ]
