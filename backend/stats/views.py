from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from stats.models import League, Team, Player, Position
from stats.serializers import LeagueSerializer, TeamSerializer, PlayerSerializer, PositionSerializer

# Create your views here.
def index(request):
  return HttpResponse("Welcome to the Statfast API!")

@csrf_exempt
def LeagueApi(request,id=0):
  if request.method=='GET':
    league = League.objects.all()
    league_serializer=LeagueSerializer(league,many=True)
    return JsonResponse(league_serializer.data, safe=False)
  elif request.method=='POST':
    league_data=JSONParser().parse(request)
    league_serializer=LeagueSerializer(data=league_data)
    if league_serializer.is_valid():
      league_serializer.save()
      return JsonResponse("Added League successfully",safe=False)
    return JsonResponse("Failed to add league",safe=False)
  elif request.method=='PUT':
    league_data=JSONParser().parse(request)
    league=League.objects.get(LeagueId=league_data['LeagueId'])
    league_serializer=LeagueSerializer(league,data=league_data)
    if league_serializer.is_valid():
      league_serializer.save()
      return JsonResponse("Update Successful", safe=False)
    return JsonResponse("Failed to update")
  elif request.method=='DELETE':
    league=League.objects.get(LeagueId=id)
    league.delete()
    return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def TeamApi(request,id=0):
  if request.method=='GET':
    team = Team.objects.all()
    team_serializer=TeamSerializer(team,many=True)
    return JsonResponse(team_serializer.data, safe=False)
  elif request.method=='POST':
    team_data=JSONParser().parse(request)
    team_serializer=TeamSerializer(data=team_data)
    if team_serializer.is_valid():
      team_serializer.save()
      return JsonResponse("Added Team successfully",safe=False)
    return JsonResponse("Failed to add team",safe=False)
  elif request.method=='PUT':
    team_data=JSONParser().parse(request)
    team=Team.objects.get(TeamId=team_data['TeamId'])
    team_serializer=TeamSerializer(team,data=team_data)
    if team_serializer.is_valid():
      team_serializer.save()
      return JsonResponse("Update Successful", safe=False)
    return JsonResponse("Failed to update team", safe=False)
  elif request.method=='DELETE':
    team=Team.objects.get(TeamId=id)
    team.delete()
    return JsonResponse("Deleted team successfully",safe=False)

@csrf_exempt
def PlayerApi(request,id=0):
  if request.method=='GET':
    team_id = request.GET.get('team_id', None)
    if team_id:
      players = Player.objects.filter(Team=team_id)
    else:
      players = Player.objects.all()
    player_serializer = PlayerSerializer(players, many=True)
    return JsonResponse(player_serializer.data, safe=False)
  elif request.method=='POST':
    player_data=JSONParser().parse(request)
    player_serializer=PlayerSerializer(data=player_data)
    if player_serializer.is_valid():
      player_serializer.save()
      return JsonResponse("Added Player successfully",safe=False)
    return JsonResponse("Failed to add player",safe=False)
  elif request.method=='PUT':
    player_data=JSONParser().parse(request)
    player=Player.objects.get(PlayerId=player_data['PlayerId'])
    player_serializer=PlayerSerializer(player,data=player_data)
    if player_serializer.is_valid():
      player_serializer.save()
      return JsonResponse("Update Successful", safe=False)
    return JsonResponse("Failed to update player", safe=False)
  elif request.method=='DELETE':
    player=Player.objects.get(PlayerId=id)
    player.delete()
    return JsonResponse("Deleted player successfully",safe=False)