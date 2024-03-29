# Generated by Django 3.1 on 2021-08-15 16:57

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome_features', '0015_auto_20210815_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pavement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pavement_Name', models.CharField(max_length=100)),
                ('Width', models.FloatField(null=True)),
                ('Shoulder_Width', models.FloatField(null=True)),
                ('Pavement_Design_Type', models.CharField(choices=[('f', 'Flexible Design'), ('r', 'Rigid Pavement')], max_length=1, null=True)),
                ('Subgrade_Density', models.FloatField(null=True)),
                ('Subgrade_Soil_Classification', models.CharField(max_length=100, null=True)),
                ('Soil_Shear_Strength', models.FloatField(null=True)),
                ('Soil_DCP_Test_Result', models.FloatField(null=True)),
                ('Soil_CPT_Test_Result', models.FloatField(null=True)),
                ('Soil_Percolation_Rate', models.FloatField(null=True)),
                ('SubBase_Material', models.CharField(max_length=100, null=True)),
                ('SubBase_Thickness', models.FloatField(null=True)),
                ('Joint_Spacing', models.FloatField(null=True)),
                ('SubBase_Base_Seperation_Material', models.CharField(max_length=100, null=True)),
                ('Base_Material', models.CharField(max_length=100, null=True)),
                ('Base_Thickness', models.CharField(max_length=100, null=True)),
                ('Concrete_Compressive_Strength', models.FloatField(null=True)),
                ('Asphalt_Thickness', models.FloatField(null=True)),
                ('Binder_Thickness', models.FloatField(null=True)),
                ('Wearing_Thickness', models.FloatField(null=True)),
                ('Drainage_Longitudinal_Slope', models.FloatField(null=True)),
                ('Drainage_Cross_Slope', models.FloatField(null=True)),
            ],
            options={
                'ordering': ['Pavement_Name'],
            },
        ),
        migrations.CreateModel(
            name='Pavement_geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('pavement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pavement_geometry', to='Aerodrome_features.pavement')),
            ],
            options={
                'ordering': ['pavement'],
            },
        ),
        migrations.AlterModelOptions(
            name='aerodrome_entity',
            options={'ordering': ['Feature_Name']},
        ),
        migrations.AlterField(
            model_name='aerodrome_entity_geometry',
            name='Entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Entity_Geometry', to='Aerodrome_features.aerodrome_entity'),
        ),
        migrations.DeleteModel(
            name='Pavement_Construction',
        ),
        migrations.AddField(
            model_name='pavement',
            name='Aerodrome_Entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Aerodrome_features.aerodrome_entity'),
        ),
    ]
