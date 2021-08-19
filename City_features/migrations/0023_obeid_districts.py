# Generated by Django 3.1 on 2021-08-17 17:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('City_features', '0022_auto_20210224_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obeid_districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('e_name', models.CharField(max_length=70)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]