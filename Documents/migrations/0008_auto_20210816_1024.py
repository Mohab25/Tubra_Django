# Generated by Django 3.1 on 2021-08-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0007_auto_20210815_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Document_file',
            field=models.FileField(upload_to='../media/documents/'),
        ),
    ]