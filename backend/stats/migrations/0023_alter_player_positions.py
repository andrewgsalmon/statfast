# Generated by Django 5.1.2 on 2024-11-22 18:54

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0022_game_winningteamid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Positions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)]), blank=True, default=None, null=True, size=None),
        ),
    ]
