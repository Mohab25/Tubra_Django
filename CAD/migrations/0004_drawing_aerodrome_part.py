# Generated by Django 3.1 on 2021-08-23 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0019_airport_parts_ob_airport'),
        ('CAD', '0003_auto_20210227_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawing',
            name='aerodrome_part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CAD_Drawing', to='Aerodrome_features.aerodrome_part'),
        ),
    ]
