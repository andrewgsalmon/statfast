from rest_framework import generics, status
from rest_framework.response import Response

from django.http import HttpResponse

from stats.models import League, Team, Player, Pitch, Play, Game
from stats.serializers import LeagueSerializer, TeamSerializer, PlayerSerializer, PitchSerializer, PlaySerializer, GameSerializer

def index(request):
  return HttpResponse("Welcome to the StatFast API!")

class LeagueListView(generics.ListCreateAPIView):
  queryset = League.objects.all()
  serializer_class = LeagueSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    response.data = {
      "message": f'Created league successfully: {response.data.get('LeagueName')}'
    }
    return response

class LeagueDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = League.objects.all()
  serializer_class = LeagueSerializer

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      league_name = serializer.data.get('LeagueName')
      custom_response = {
        "message": f"League name updated successfully to {league_name}."
      }
      return Response(custom_response, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update league.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    league_name = instance.LeagueName
    instance.delete()
    return Response({"message": f"{league_name} deleted successfully."}, status=status.HTTP_202_ACCEPTED)

class TeamListCreateView(generics.ListCreateAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    response.data = {
      "message": f"Created team successfully: {response.data.get('TeamName')}"
    }
    return response

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      team_name = serializer.data.get('TeamName')
      custom_response = {
        "message": f"{team_name} updated successfully.",
        "data": serializer.data
      }
      return Response(custom_response, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update team.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    team_name = instance.TeamName
    instance.delete()
    return Response({"message": f"{team_name} deleted successfully."}, status=status.HTTP_202_ACCEPTED)

class PlayerListCreateView(generics.ListCreateAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    response.data = {
      "message": f"Added {response.data.get('FirstName')} {response.data.get('LastName')} successfully"
    }
    return response

class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      player_name = f"{serializer.data.get('FirstName')} {serializer.data.get('LastName')}"
      custom_response = {
        "message": f"{player_name} updated successfully.",
        "data": serializer.data
      }
      return Response(custom_response, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update player.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    player_name = instance.PlayerName
    instance.delete()
    return Response({"message": f"{player_name} deleted successfully."}, status=status.HTTP_202_ACCEPTED)

class PitchListCreateView(generics.ListCreateAPIView):
  queryset = Pitch.objects.all()
  serializer_class = PitchSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    response.data = {
      "message": "Created pitch successfully"
    }
    return response

class PitchDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pitch.objects.all()
  serializer_class = PitchSerializer

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      custom_response = {
        "message": "Pitch updated successfully.",
        "data": serializer.data
      }
      return Response(custom_response, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update pitch.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    player_name = instance.PlayerName
    instance.delete()
    return Response({"message": f"{player_name} deleted successfully."}, status=status.HTTP_202_ACCEPTED)

class GamePitchesListView(generics.ListAPIView):
  serializer_class = PitchSerializer

  def get_queryset(self):
    game_id = self.kwargs.get('game_id')
    return Pitch.objects.filter(GameId=game_id)

class GameListCreateView(generics.ListCreateAPIView):
  queryset = Game.objects.all()
  serializer_class = GameSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    response.data = {
      "message": "Created new game successfully"
    }
    return response

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  serializer_class = GameSerializer

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      custom_response = {
        "message": "Game updated successfully.",
        "data": serializer.data
      }
      return Response(custom_response, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update game.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response({"message": "Game deleted successfully."}, status=status.HTTP_202_ACCEPTED)

class PlayListCreateView(generics.ListCreateAPIView):
  queryset = Play.objects.all()
  serializer_class = PlaySerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    response.data = {
      "message": "Created new play successfully"
    }
    return response

class PlayDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Play.objects.all()
  serializer_class = PlaySerializer

  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      custom_response = {
        "message": "Updated play successfully.",
        "data": serializer.data
      }
      return Response(custom_response, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update play.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response({"message": "Play deleted successfully."}, status=status.HTTP_202_ACCEPTED)

class GamePlaysListView(generics.ListAPIView):
  serializer_class = PlaySerializer

  def get_queryset(self):
    game_id = self.kwargs.get('game_id')
    return Play.objects.filter(GameId=game_id)