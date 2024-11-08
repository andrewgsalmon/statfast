from django.db import models

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
  LastName = models.CharField(max_length=500, default="not set")
  Team = models.PositiveIntegerField()
  Positions = models.ManyToManyField(Position)
  Bats = models.CharField(max_length=1)
  Throws = models.CharField(max_length=1)

  def __str__(self):
      return [self.LastName, self.FirstName]
