# Generated by Django 3.1 on 2021-02-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0004_auto_20210225_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Document_file',
            field=models.FileField(max_length=500, upload_to=''),
        ),
    ]