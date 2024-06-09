import lxml
import requests
from bs4 import BeautifulSoup
import re
import time


player_name = input("Player Name: ")
try:
    link = f"https://www.google.com/search?q={player_name}+premier+league.com+stats"
    source = requests.get(link).text
    page = BeautifulSoup(source, "lxml")
    page = page.find("div",class_="kCrYT")
    link = page.find("a", href=re.compile(r"[/]([a-z]|[A-Z])\w+")).attrs["href"]

except:
    link = f"https://www.google.com/search?q={player_name}+p+stats"
    source = requests.get(link).text
    page = BeautifulSoup(source, "lxml")
    page = page.find("div",class_="kCrYT")
    link = page.find("a", href=re.compile(r"[/]([a-z]|[A-Z])\w+")).attrs["href"]

spl_word = '&sa'
res = link[7:].partition(spl_word)[0]

if "stats" in res:
    res = res.replace('stats','overview')


sta = res.replace('overview','stats')
source = requests.get(sta).text
page = BeautifulSoup(source, "lxml")
side = page.find("div",class_="label").text


###
name = page.find("div",class_="name t-colour").text
position = page.find("div",class_="info").text.strip()
club = "No longer part of EPL"


if "Club" in side:
    a = page.find_all("div",class_="info")
    club = page.find("div",class_="info").text.strip()
    position = a[1].text.strip()

    
    
    


#####
stats = page.find_all("div",class_="topStat")
basic = []

for i in range(len(stats)):
    basic.append(stats[i].text.strip())

basic_stats = []

for k in range(len(final)):
    basic_stats.append(basic[k].split("\n"))




####
source2 = requests.get(res).text
page2 = BeautifulSoup(source2, "lxml")
personal_details = page2.find("div",class_="playerInfo")
pd = personal_details.find_all("div",class_="info")



####
nationality = personal_details.find("span",class_="playerCountry").text
dob = pd[1].text.strip()
try:
    height = pd[2].text.strip()
    print(height)
except:
    pass
###



fin = page.find_all("div",class_="normalStat")

final=[]

for j in range(len(fin)):
    final.append(fin[j].text.strip())


###
all_stats = []

for k in range(len(final)):
    all_stats.append(final[k].split("\n"))








