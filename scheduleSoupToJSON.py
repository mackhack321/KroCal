from scheduleToSoup import getScheduleSoup
from bs4 import BeautifulSoup
import json

def makeJSON(args): # get soup and dump it to a JSON file
    soup = getScheduleSoup()
    dates = soup.find("div",{"class":"dates"})
    if args == "--latest":
        firstrow = dates.find("ul",{"class":"days row even min last-child week2 lastweek"})
        blocks = firstrow.find_all("li")
    else:
        try:
            firstrow = dates.find("ul",{"class":"days row even alert min last-child week3 lastweek"})
            blocks = firstrow.find_all("li")
        except AttributeError:
            firstrow = dates.find("ul",{"class":"days row even min last-child week3 lastweek"})
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
    json.dump(mydict,open("hours.json","w"),indent = 4)
if __name__ == "__main__": makeJSON()
