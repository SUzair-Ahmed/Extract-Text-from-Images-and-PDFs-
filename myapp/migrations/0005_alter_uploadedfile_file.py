# Generated by Django 5.0.7 on 2024-07-22 21:55

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_uploadedfile_delete_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to=myapp.models.upload_to),
        ),
    ]
