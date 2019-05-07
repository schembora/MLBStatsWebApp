import requests
import json
from pymongo import MongoClient
from functools import reduce


client = MongoClient("mongodb://admin:Qazedc123!@ds151086.mlab.com:51086/heroku_q37d8qnw")

db = client["heroku_q37d8qnw"]
posts = db.teams
posts1 = db.hitters
posts2=  db.pitchers

#

URLTeam = "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2019'"
URLEachTeam = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id="
URLSeasonBatting = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='2019'&player_id="
URLSeasonPitching = "http://lookup-service-prod.mlb.com/json/named.sport_pitching_tm.bam?league_list_id='mlb'&game_type='R'&season='2019'&player_id="
location = "Rutgers University"
PARAMS = {'address':location} 
r = requests.get(url = URLTeam, params = PARAMS)

data = r.json()

#print(data)


#Need function to update data everyday

#update putcher stats
'''for post in posts.find():
    newURL = URLEachTeam + "\'" + post["team_id"] + "\'"
    req = requests.get(url = newURL, params = PARAMS)
    for element in req.json()["roster_40"]["queryResults"]["row"]:
        newURL1 = URLSeasonPitching + "\'" + element["player_id"] + "\'"
        req1 = requests.get(url = newURL1, params = PARAMS)
        newElement = req1.json()["sport_pitching_tm"]["queryResults"]
        if int(newElement["totalSize"]) == 1:
                #result = posts2.insert_one(newElement["row"])   
            result = posts2.update_one({"player_id": newElement["row"]["player_id"]}, {"$set": newElement["row"]})
#update hitter stats
for post in posts.find():
        newURL = URLEachTeam + "\'" + post["team_id"] + "\'"
        req = requests.get(url = newURL, params = PARAMS)
        for element in req.json()["roster_40"]["queryResults"]["row"]:
            newURL1 = URLSeasonBatting + "\'" + element["player_id"] + "\'"
            req1 = requests.get(url = newURL1, params = PARAMS)
            newElement = req1.json()["sport_hitting_tm"]["queryResults"]
            if int(newElement["totalSize"]) == 1:
                    #result = posts1.insert_one(newElement["row"])
                result =  posts1.update_one({"player_id": newElement["row"]["player_id"]}, {"$set": newElement["row"]})
'''
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

def avgStatsHitters():
    avgAList = db.hitters.distinct('avg')
    avgAList = [x for x in avgAList if x!= ".---"]
    avgAvg = round(reduce(lambda x, y: float(x)+float(y), avgAList)/ len(avgAList), 3)
    avgOList = db.hitters.distinct("obp")
    avgOList = [x for x in avgOList if x!= ".---"]
    avgObp = round(reduce(lambda x, y: float(x)+float(y), avgOList)/ len(avgOList), 3)
    return [avgAvg, avgObp]

def avgStatsPitchers():
    avgEList = db.pitchers.distinct('era')
    avgEList = [x for x in avgEList if x!= "*.**"]
    avgEra = round(reduce(lambda x, y: float(x)+float(y), avgEList)/ len(avgEList),2)
    avgWList = db.pitchers.distinct('whip')
    avgWList = [x for x in avgWList if x!= "*.**"]
    avgWhip = round(reduce(lambda x, y: float(x)+float(y), avgWList)/ len(avgWList),2)
    return [avgEra, avgWhip]

avgStatsPitchers()
