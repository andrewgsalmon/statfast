# Generated by Django 5.1.2 on 2024-11-15 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0016_play_fieldingsequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='FielderOnHit',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(9)]),
        ),
    ]
