from rest_framework import serializers
from stats.models import League, Team, Position, Player

class LeagueSerializer(serializers.ModelSerializer):
  class Meta:
    model=League
    fields=('LeagueId', 'LeagueName')

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model=Team
    fields=('TeamId', 'TeamName', 'League')

class PositionSerializer(serializers.ModelSerializer):
  class Meta:
    model=Position
    fields=('name', 'position_number')

class PlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model=Player
    fields=('PlayerId', 'PlayerName', 'Team', 'Positions')