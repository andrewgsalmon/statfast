# Generated by Django 5.1.2 on 2024-11-11 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='JerseyNumber',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='LastName',
            field=models.CharField(max_length=500),
        ),
    ]