# Generated by Django 3.1 on 2021-08-23 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0019_airport_parts_ob_airport'),
        ('Employee', '0003_auto_20210815_1657'),
        ('CAD', '0006_auto_20210823_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='Aerodrome_Entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CAD_Drawing', to='Aerodrome_features.aerodrome_entity'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='Author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CAD_Drawing', to='Employee.employee'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='CAD_file',
            field=models.ImageField(blank=True, max_length=700, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='Date_of_Authorization',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='Drawing_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawing_series', to='CAD.drawingseries'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='Number_of_issuance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='aerodrome_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CAD_Drawing', to='Aerodrome_features.aerodrome_part'),
        ),
    ]
