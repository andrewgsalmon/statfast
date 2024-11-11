from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.index, name='index'),
    path('leagues', views.LeagueApi, name='leagues'),
    path('leagues/<int:id>', views.LeagueApi, name='league_detail'),
    path('teams', views.TeamApi, name='teams'),
    path('teams/<int:id>', views.TeamApi, name='team_detail'),
    path('players', views.PlayerApi, name='players'),
    path('players/<int:id>', views.PlayerApi, name='player_detail'),
    path('pitches', views.PitchApi, name='pitches'),
    path('games', views.GameApi, name='games')
]