import pandas as pd
import datetime
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import requests

teams=["TOR","CHO","ATL","DEN","BRK","BOS","CHI","CLE","DAL","DET","GSW","LAL","HOU","IND","LAC","MEM","MIA","WAS","UTA","SAS","SAC","POR","PHO","PHI","ORL","NYK","OKC","MIL","MIN","NOP"]

def player_info(name):
    year = datetime.date.today().year
    link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
    site=requests.get(link)
    html_text=site.content
    html_site=BeautifulSoup(html_text,"lxml")
    links=html_site.tbody
    player_links=[]
    for i in links.find_all("a"):
        if "players" in i.get("href"):
            player_links.append(i.get("href"))
    return player_links


def team(name):
    year = datetime.date.today().year
    link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
    df=pd.read_html(link, match="Per Game")#Table containing all the data of the team's player's career (divided by the number of games they've played)
    df=df[0]
    team=[]
    age=list(df["Age"])
    names=list(df["Unnamed: 1"])#names of all members in the team
    three_pt_p=list(df["3P%"])#Three pts percent per game
    two_pt_p=list(df["2P%"])#2 pt percent per game
    field_goal_p=list(df["FG%"])#field goal percent
    freethrowpercent=list(df["FT%"])
    pts_per_game=list(df["PTS/G"])#avg pts per game
    offensive_rebound=list(df["ORB"])#Offensive Rebounds per game
    defensive_rebounds=list(df["DRB"])#Defensive Rebounds per game
    total_rebounds=list(df["TRB"])#Total Rebounds per game
    steals=list(df["STL"])#Steals per game 
    blocks=list(df["BLK"])#Blocks per game
    assists=list(df["AST"])
    games=list(df["G"])
    dft=pd.read_html(link,match="Roster")
    dft=dft[0]
    namestwo=list(dft["Player"])
    personal_pages=player_info(name)
    while len(names)!=0:
        person={"name":None,"age":None,"field goal percent":None,"free throw percent":None,"2 Point Percent":None,"3 Point Percent":None,"PTS per game":None,"orb":None,"drb":None,"total rebounds":None,"steals":None,"blocks":None,"assists":None,"games":None,"link":None}
        person["name"]=names.pop(0)
        person["age"]=age.pop(0)
        person["field goal percent"]=field_goal_p.pop(0)
        person["free throw percent"]=freethrowpercent.pop(0)
        person["2 Point Percent"]=two_pt_p.pop(0)
        person["3 Point Percent"]=three_pt_p.pop(0)
        person["PTS per game"]=pts_per_game.pop(0)
        person["orb"]=offensive_rebound.pop(0)
        person["drb"]=defensive_rebounds.pop(0)
        person["total rebounds"]=total_rebounds.pop(0)
        person["blocks"]=blocks.pop(0)
        person["steals"]=steals.pop(0)
        person["assists"]=assists.pop(0)
        person["games"]=games.pop(0)
        team.append(person)
        if person["name"] in namestwo:
            ind=namestwo.index(person["name"])
            person["link"]="https://www.basketball-reference.com{}".format(personal_pages[ind])
    return team


def extract_player(team_name,player_name):
    p=team(team_name)
    for i in p:
        if player_name in i["name"]:
            return i
    return None


def total_player_stats(name,player):
    links=player_info(name)
    link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
    df=pd.read_html(link, match="Per Game")#Table containing all the data of the team's player's career (divided by the number of games they've played)
    df=df[0]
    name=list(df["Unnamed: 1"])
    p=None
    for i in name:
        if player in i:
            p=name.index(i)
            break


def graph_maker(name,stat): 
    assert stat!="name"
    p=team(name)
    year = datetime.date.today().year
    link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
    df=pd.read_html(link, match="Per Game")#Table containing all the data of the team's player's career (divided by the number of games they've played)
    df=df[0]
    name=list(df["Unnamed: 1"])
    measured_stat=[]
    for i in p:
        measured_stat.append(i[stat])
    plt.plot(name,measured_stat)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.ylim(0,1.25)
    plt.show()

def test():
    n=0
    no_link=[]
    for i in teams:
        p=team(i)
        print(i)
        team1=[]
        for i in p:
            n+=1
            if i["link"]==None:
                team1.append(i)
        no_link.append(team1)
        print(n)
    print(len(no_link))
test()