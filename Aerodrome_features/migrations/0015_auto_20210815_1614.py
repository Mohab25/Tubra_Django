# Generated by Django 3.1 on 2021-08-15 16:14

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0014_auto_20210815_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aerodrome_entity',
            name='geom',
        ),
        migrations.CreateModel(
            name='Aerodrome_Entity_Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('Entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Entity_Geometry', to='Aerodrome_features.aerodrome_entity')),
            ],
        ),
    ]
