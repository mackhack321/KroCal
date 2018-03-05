from scheduleToSoup import getScheduleSoup
from bs4 import BeautifulSoup
import json
#soup = getScheduleSoup()
site = open("temphtml.html").read()
soup = BeautifulSoup(site,features="lxml")

dates = soup.find("div",{"class":"dates"})
firstrow = dates.find("ul",{"class":"days row odd max first-child week1"})
blocks = firstrow.find_all("li")
blocks.remove(blocks[len(blocks)-1])
mydict = {}
for block in blocks:
    date = block.div.span.text
    try:
        hours = block.find("span",{"class":"hours"}).text
        mydict[date] = hours
    except:
        mydict[date] = "off"
secondrow = dates.find("ul",{"class":"days row even min last-child week2 lastweek"})
blocks = secondrow.find_all("li")
blocks.remove(blocks[len(blocks)-1])
for block in blocks:
    date = block.div.span.text
    try:
        hours = block.find("span",{"class":"hours"}).text
        mydict[date] = hours
    except:
        mydict[date] = "off"
print(mydict)
json.dump(mydict,open("hours.json","w"),indent = 4)
