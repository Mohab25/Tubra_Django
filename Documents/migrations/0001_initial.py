# Generated by Django 3.1 on 2020-09-19 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document_file', models.FileField(upload_to='')),
                ('document_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents', to='Documents.documenttype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
