from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('search.html', views.search, name="search"),
    path('searchPlayer', views.searchPlayers, name="searchPlayers"),
    path('teamList.html', views.teamList, name="teamList"),
    path('team/team-<parameter>.html', views.team, name = "team"),
    path('player/player-<parameter>.html', views.player, name = "player")
]