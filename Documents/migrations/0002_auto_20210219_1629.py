# Generated by Django 3.1 on 2021-02-19 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aerodrome', '0001_initial'),
        ('Aerodrome_features', '0001_initial'),
        ('Documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['pk']},
        ),
        migrations.RenameField(
            model_name='document',
            old_name='document_file',
            new_name='Document_file',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='name',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='document',
            name='document_type',
        ),
        migrations.AddField(
            model_name='document',
            name='Aerodrome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reports', to='Aerodrome.aerodrome'),
        ),
        migrations.AddField(
            model_name='document',
            name='Aerodrome_Entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reports', to='Aerodrome_features.aerodrome_entity'),
        ),
        migrations.DeleteModel(
            name='DocumentType',
        ),
        migrations.AddField(
            model_name='document',
            name='Document_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Reports', to='Documents.document_type'),
        ),
    ]
