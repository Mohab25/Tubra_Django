# Generated by Django 3.1 on 2021-08-15 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0013_remove_aerodrome_part_geom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aerodrome_part',
            options={'ordering': ['Name']},
        ),
    ]
