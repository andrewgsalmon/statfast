from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.index, name='index'),
    path('leagues', views.LeagueListView.as_view(), name='leagues'),
    path('leagues/<int:pk>', views.LeagueDetailView.as_view(), name='league_detail'),
    path('teams', views.TeamListCreateView.as_view(), name='teams'),
    path('teams/<int:pk>', views.TeamDetailView.as_view(), name='team_detail'),
    path('players', views.PlayerListCreateView.as_view(), name='players'),
    path('players/<int:pk>', views.PlayerDetailView.as_view(), name='player_detail'),
    path('pitches', views.PitchListCreateView.as_view(), name='pitches'),
    path('pitches/<int:pk>', views.PitchDetailView.as_view(), name='pitches'),
    path('pitches/game/<int:game_id>', views.GamePitchesListView.as_view(), name='pitches_by_game'),
    path('games', views.GameListCreateView.as_view(), name='games'),
    path('games/<int:pk>', views.GameDetailView.as_view(), name='games'),
    path('plays', views.PlayListCreateView.as_view(), name='plays'),
    path('plays/<int:pk>', views.PlayDetailView.as_view(), name='play_detail'),
    path('plays/game/<int:game_id>', views.GamePlaysListView.as_view(), name='plays_by_game')
]