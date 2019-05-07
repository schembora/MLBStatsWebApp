from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mlb_app import getData
from django.template import loader, Context
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import BarChart


def index(request):
    #return HttpResponse("Gerrit Cole's era is: " + getData.getPitcherByName("Gerrit Cole")["era"])
    '''t = loader.get_template("mlb_app/base.html")
    teams = getData.getTeams()
    html = t.render({"teams": teams})  
    return HttpResponse(html)   
    '''
    t = loader.get_template("mlb_app/home.html")
    html = t.render()
    return HttpResponse(html)

def teamList(request):
    t = loader.get_template("mlb_app/teamlist.html")
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
        if playerStats != None:
            data = getData.avgStatsPitchers()
            graphData = [ 
                ["Stat", player["name_display_first_last"], "MLB Average"],
                ['ERA', float(playerStats['era']), data[0]],
                ['WHIP', float(playerStats['whip']), data[1]]
            ]
    else:
        data = getData.avgStatsHitters()
        playerStats = getData.getHitterByID(parameter)
        if playerStats != None:
            graphData = [ 
                ['Stat', player["name_display_first_last"], 'MLB Average'],
                ['Average', round(float(playerStats["avg"]),3), data[0]],
                ['On Base Percentage', round(float(playerStats["obp"]),3), data[1] ]
            ]
    if playerStats != None:
        data_source = SimpleDataSource(data=graphData)
        chart = BarChart(data_source, width="100%")
        html = t.render({'player': player, 'playerStats': playerStats, 'chart': chart})
    else:
        html = t.render({'player': player, 'playerStats': playerStats})
    return HttpResponse(html)

