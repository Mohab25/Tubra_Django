# Generated by Django 3.1 on 2021-02-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('City_features', '0018_city_facility_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city_facility',
            name='Category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
