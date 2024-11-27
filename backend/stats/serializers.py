from rest_framework import serializers
from stats.models import League, Team, Position, Player, Pitch, Game, Play

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
    fields=('name', 'position_number', 'abbrev')

class PlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model=Player
    fields=('PlayerId', 'FirstName', 'LastName', 'Team', 'Positions', 'Bats', 'Throws', 'JerseyNumber')

class PitchSerializer(serializers.ModelSerializer):
  class Meta:
    model=Pitch
    fields=('PitchId', 'GameId', 'PitcherId', 'BatterId', 'PitchType', 'PitchCall', 'PitchLocation', 'SwingType', 'Contact', 'PlayId')

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model=Game
    fields=('GameId', 'Date', 'VisitingTeamId', 'HomeTeamId', 'WinningTeamId', 'LeagueId')

class PlaySerializer(serializers.ModelSerializer):
  class Meta:
    model=Play
    fields=('PlayId', 'GameId', 'BatterId', 'PitcherId', 'TotalBases', 'PlayType', 'BallInPlayType', 'FielderOnHit', 'FieldingSequence', 'OutsRecorded', 'BasesAdvancedFromFirst', 'BasesAdvancedFromSecond', 'BasesAdvancedFromThird', 'Runs', 'EarnedRuns', 'PlayersScored', 'Errors')