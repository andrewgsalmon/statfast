# Generated by Django 5.1.2 on 2024-11-15 04:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0011_remove_play_errors'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='Errors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
            preserve_default=False,
        ),
    ]
