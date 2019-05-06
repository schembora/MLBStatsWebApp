from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mlb_app import getData
from django.template import loader, Context


def index(request):
    #return HttpResponse("Gerrit Cole's era is: " + getData.getPitcherByName("Gerrit Cole")["era"])
    '''t = loader.get_template("mlb_app/base.html")
    teams = getData.getTeams()
    html = t.render({"teams": teams})  
    return HttpResponse(html)   
    '''
    t = loader.get_template("mlb_app/index.html")
    html = t.render()
    return HttpResponse(html)

def teamList(request):
    t = loader.get_template("mlb_app/base.html")
    teams = getData.getTeams()
    html = t.render({"teams": teams})  
    return HttpResponse(html)  

def team(request, parameter):
    t = loader.get_template("mlb_app/team.html")
    team = getData.getTeamByTeamID(parameter)
    players = getData.getPlayersByTeamID(parameter)
    html = t.render({"team" : team, "players": players})
    return HttpResponse(html)

def player(request, parameter):
    t = loader.get_template("mlb_app/player.html")
    player = getData.getPlayerByID(parameter)   
    if "P" in player['position_txt']:
        playerStats = getData.getPitcherByID(parameter)
    else:
        playerStats = getData.getHitterByID(parameter)
    html = t.render({'player': player, 'playerStats': playerStats})
    return HttpResponse(html)

