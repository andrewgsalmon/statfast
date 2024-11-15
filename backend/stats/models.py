from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here.

class League(models.Model):
  LeagueId = models.AutoField(primary_key=True)
  LeagueName = models.CharField(max_length=500)

class Team(models.Model):
  TeamId = models.AutoField(primary_key=True)
  TeamName = models.CharField(max_length=500)
  League = models.PositiveIntegerField()

class Position(models.Model):
  name = models.CharField(max_length=100)
  position_number = models.PositiveIntegerField(unique=True)

  def __str__(self):
      return f"{self.position_number} - {self.name}"

class Player(models.Model):
  PlayerId = models.AutoField(primary_key=True)
  FirstName = models.CharField(max_length=500)
  LastName = models.CharField(max_length=500)
  JerseyNumber = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
  Team = models.PositiveIntegerField()
  Positions = models.ManyToManyField(Position)
  Bats = models.CharField(max_length=1)
  Throws = models.CharField(max_length=1)

  def __str__(self):
      return [self.LastName, self.FirstName]

class Pitch(models.Model):
  PitchId = models.AutoField(primary_key=True)
  GameId = models.PositiveIntegerField()
  PitcherId = models.PositiveIntegerField()
  BatterId = models.PositiveIntegerField()
  Outs = models.PositiveIntegerField()
  PitchType = models.CharField(max_length=100)
  PitchCall = models.CharField(max_length=100)
  PitchLocation = ArrayField(base_field=models.CharField(max_length=50), size=2)
  SwingType = models.CharField(default="take", blank=True)
  Contact = models.BooleanField(default=False, blank=True)
  PlayId = models.IntegerField(default=None, blank=True, null=True)
  BallInPlayType = models.CharField(max_length=100, null=True, blank=True, default=None)

class Play(models.Model):
  PlayId = models.AutoField(primary_key=True)
  GameId = models.PositiveIntegerField()
  BatterId = models.IntegerField()
  PitcherId = models.IntegerField()
  TotalBases = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, default=0)
  PlayType = models.CharField(max_length=100)
  BallInPlayType = models.CharField(max_length=100)
  OutsRecorded = models.IntegerField(validators=[MaxValueValidator(3)], blank=True, default=0)
  Runs = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, default=0)
  EarnedRuns = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, default=0)
  PlayersScored = ArrayField(base_field=models.IntegerField())
  Errors = models.JSONField()

class Game(models.Model):
  GameId = models.AutoField(primary_key=True)
  Date = models.DateField()
  VisitingTeamId = models.PositiveIntegerField()
  HomeTeamId = models.PositiveIntegerField()
  LeagueId = models.PositiveIntegerField()
