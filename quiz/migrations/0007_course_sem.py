# Generated by Django 3.2.5 on 2023-10-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20231006_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sem',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
