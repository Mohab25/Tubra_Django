# Generated by Django 3.1 on 2021-08-15 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome', '0001_initial'),
        ('Aerodrome_features', '0017_auto_20210815_1928'),
        ('Documents', '0006_auto_20210228_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='aerodrome_part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Documents', to='Aerodrome_features.aerodrome_part'),
        ),
        migrations.AlterField(
            model_name='document',
            name='Aerodrome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Documents', to='Aerodrome.aerodrome'),
        ),
        migrations.AlterField(
            model_name='document',
            name='Aerodrome_Entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Documents', to='Aerodrome_features.aerodrome_entity'),
        ),
    ]