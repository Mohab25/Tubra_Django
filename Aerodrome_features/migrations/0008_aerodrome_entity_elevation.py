# Generated by Django 3.1 on 2021-02-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0007_auto_20210224_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerodrome_entity',
            name='Elevation',
            field=models.FloatField(null=True),
        ),
    ]
