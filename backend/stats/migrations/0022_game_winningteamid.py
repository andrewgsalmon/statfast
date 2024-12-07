# Generated by Django 5.1.2 on 2024-11-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_alter_position_abbrev'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='WinningTeamId',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS stats_player_Positions;",
            reverse_sql="SELECT 1;"
        ),
    ]