# Generated by Django 3.1 on 2021-08-16 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0017_auto_20210815_1928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aerodrome_entity',
            options={'ordering': ['Feature_Name'], 'verbose_name_plural': 'Aerodrome Entities'},
        ),
        migrations.AlterModelOptions(
            name='aerodrome_entity_category',
            options={'ordering': ['Name'], 'verbose_name_plural': 'Aerodrome Entity Categories'},
        ),
        migrations.AlterModelOptions(
            name='aerodrome_entity_geometry',
            options={'ordering': ['Entity'], 'verbose_name_plural': 'Aerodrome Entities Geometries'},
        ),
        migrations.AlterModelOptions(
            name='aerodrome_entity_image',
            options={'ordering': ['id'], 'verbose_name_plural': 'Aerodrome Entities Images'},
        ),
        migrations.AlterModelOptions(
            name='aerodrome_part',
            options={'ordering': ['Name'], 'verbose_name_plural': 'Aerodrome Parts'},
        ),
        migrations.AlterModelOptions(
            name='pavement',
            options={'ordering': ['Pavement_Name'], 'verbose_name_plural': 'Pavements'},
        ),
        migrations.AlterModelOptions(
            name='pavement_geometry',
            options={'ordering': ['pavement'], 'verbose_name_plural': 'Pavements Geometries'},
        ),
    ]