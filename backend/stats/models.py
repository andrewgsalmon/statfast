from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class League(models.Model):
  LeagueId = models.AutoField(primary_key=True)
  LeagueName = models.CharField(max_length=500)

  def __str__(self):
    return f"{self.LeagueName}"

class Team(models.Model):
  TeamId = models.AutoField(primary_key=True)
  TeamName = models.CharField(max_length=500)
  League = models.PositiveIntegerField()

def __str__(self):
  return f"{self.TeamName}"

class Position(models.Model):
  name = models.CharField(max_length=100)
  abbrev = models.CharField(max_length=2)
  position_number = models.PositiveIntegerField(unique=True)

  def __str__(self):
    return f"{self.position_number} - {self.name}"

class Player(models.Model):
  PlayerId = models.AutoField(primary_key=True)
  FirstName = models.CharField(max_length=500)
  LastName = models.CharField(max_length=500)
  JerseyNumber = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
  Team = models.PositiveIntegerField()
  Positions = ArrayField(base_field=models.PositiveIntegerField(validators=[MaxValueValidator(10)]), null=True, default=None, blank=True)
  Bats = models.CharField(max_length=1)
  Throws = models.CharField(max_length=1)

  def __str__(self):
    return f"Added {self.FirstName} {self.LastName} to team {self.Team}"

class Pitch(models.Model):
  PitchId = models.AutoField(primary_key=True)
  GameId = models.PositiveIntegerField()
  PitcherId = models.PositiveIntegerField()
  BatterId = models.PositiveIntegerField()
  PitchType = models.CharField(max_length=100)
  PitchCall = models.CharField(max_length=100)
  PitchLocation = ArrayField(base_field=models.CharField(max_length=50), size=2)
  SwingType = models.CharField(default="take", blank=True)
  Contact = models.BooleanField(default=False, blank=True)
  PlayId = models.IntegerField(default=None, blank=True, null=True)

  def __str__(self):
    return f"Added pitch by {self.PitcherId} to game {self.GameId}"

class Play(models.Model):
  PlayId = models.AutoField(primary_key=True)
  GameId = models.PositiveIntegerField()
  BatterId = models.IntegerField()
  PitcherId = models.IntegerField()
  TotalBases = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, default=0)
  PlayType = models.CharField(max_length=100)
  BallInPlayType = models.CharField(max_length=100)
  FielderOnHit = models.IntegerField(validators=[MaxValueValidator(9)], blank=True, null=True, default=None)
  FieldingSequence = ArrayField(base_field=models.IntegerField(), blank=True, null=True, default=list)
  OutsRecorded = models.IntegerField(validators=[MaxValueValidator(3)], blank=True, default=0)
  BasesAdvancedFromFirst = models.IntegerField(validators=[MaxValueValidator(3)], blank=True, null=True, default=None)
  BasesAdvancedFromSecond = models.IntegerField(validators=[MaxValueValidator(2)], blank=True, null=True, default=None)
  BasesAdvancedFromThird = models.IntegerField(validators=[MaxValueValidator(1)], blank=True, null=True, default=None)
  Runs = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, default=0)
  EarnedRuns = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, default=0)
  PlayersScored = ArrayField(base_field=models.IntegerField(), blank=True, null=True, default=list)
  Errors = ArrayField(base_field=models.IntegerField(), blank=True, null=True, default=list)

  def __str__(self):
    return f"Added play to game {self.GameId}"

class Game(models.Model):
  GameId = models.AutoField(primary_key=True)
  Date = models.DateField()
  VisitingTeamId = models.PositiveIntegerField()
  HomeTeamId = models.PositiveIntegerField()
  WinningTeamId = models.PositiveBigIntegerField()
  LeagueId = models.PositiveIntegerField()
