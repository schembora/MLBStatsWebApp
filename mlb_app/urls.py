from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('team/team-<parameter>.html', views.team, name = "team"),
    path('player/player-<parameter>.html', views.player, name = "player")
]