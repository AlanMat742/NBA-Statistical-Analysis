import requests
import os.path
import os
from bs4 import BeautifulSoup
import datetime
year = datetime.date.today().year
def player_info_hrefs(name):
    link="https://www.basketball-reference.com/teams/{}/{}.html".format(name,year)
    site=requests.get(link)
    html_text=site.content
    html_site=BeautifulSoup(html_text,"lxml")
    links=html_site.tbody
    player_raw_link=[]
    for i in links.find_all("a"):
        if "players" in i.get("href"):
            link=i.get("href").split("/")
            val=link[-1]
            player_raw_link.append(val[:-5])
    return player_raw_link

teams=["TOR","CHO","ATL","DEN","BRK","BOS","CHI","CLE","DAL","DET","GSW","LAL","HOU","IND","LAC","MEM","MIA","WAS","UTA","SAS","SAC","POR","PHO","PHI","ORL","NYK","OKC","MIL","MIN","NOP"]
for i in teams:
    team=player_info_hrefs(i)
    save_path = ''#Edit this to some file directory on ur computer
    for i in team:
        completeName = os.path.join(save_path,"{}.jpg".format(i))         
        pic=requests.get("https://www.basketball-reference.com/req/202102081/images/players/{}.jpg".format(i)) 
        file1 = open(completeName, "wb")
        file1.write(pic.content)
        file1.close()
