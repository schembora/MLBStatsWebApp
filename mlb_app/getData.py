import requests
import json
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.mlb_data
posts = db.teams

posts1 = db.hitters
posts2=  db.pitchers

#
'''
URLTeam = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2019'"
URLEachTeam = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id="
URLSeasonBatting = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='2019'&player_id="
URLSeasonPitching = "http://lookup-service-prod.mlb.com/json/named.sport_pitching_tm.bam?league_list_id='mlb'&game_type='R'&season='2019'&player_id="
location = "Rutgers University"
PARAMS = {'address':location} 
r = requests.get(url = URLTeam, params = PARAMS)

data = r.json()
'''
#print(data)



# adding each team to database
#for element in data["team_all_season"]["queryResults"]["row"]:
    #result = posts.insert_one(element)

# add each player to players database
'''for post in posts.find():
    newURL = URLEachTeam + "\'" + post["team_id"] + "\'"
    req = requests.get(url = newURL, params = PARAMS)
    for element in req.json()["roster_40"]["queryResults"]["row"]:
        db.totalPlayers.insert_one(element)
'''

'''
for post in posts.find():
    newURL = URLEachTeam + "\'" + post["team_id"] + "\'"
    req = requests.get(url = newURL, params = PARAMS)
    for element in req.json()["roster_40"]["queryResults"]["row"]:
        newURL1 = URLSeasonPitching + "\'" + element["player_id"] + "\'"
        req1 = requests.get(url = newURL1, params = PARAMS)
        newElement = req1.json()["sport_pitching_tm"]["queryResults"]
        if int(newElement["totalSize"]) == 1:
            result = posts2.insert_one(newElement["row"])
'''
#add batting stats to each player


#Need to write function which will update player stats everyday
def getHitterByName(name):
    return db.hitters.find_one({"player_id": db.totalPlayers.find_one({"name_display_first_last": name})["player_id"]})
def getPlayerByName(name):
    return db.totalPlayers.find_one({"name_display_first_last": name})
def getPitcherByName(name):
    return db.pitchers.find_one({"player_id": db.totalPlayers.find_one({"name_display_first_last": name})["player_id"]})
def getTeams():
    return db.teams.find()
def getPlayersByTeamID(teamID):
    return db.totalPlayers.find({"team_id":teamID})
def getTeamByTeamID(teamID):
    return db.teams.find_one({"team_id": teamID})
def getPlayerByID(playerID):
    return db.totalPlayers.find_one({"player_id": playerID})
def getPitcherByID(playerID):
    return db.pitchers.find_one({"player_id": playerID})
def getHitterByID(playerID):
    return db.hitters.find_one({"player_id": playerID})
