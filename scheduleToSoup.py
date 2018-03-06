from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
from bs4 import BeautifulSoup
def getScheduleSoup(): # get bs4 object of schedule portal data
    jsondata = json.load(open("krologin.json"))
    krousr = jsondata["login"]
    kropass = jsondata["pass"]
    # init browser, open website, find login field
    driver = webdriver.Chrome()
    driver.get("http://greatpeople.me")
    userfield = driver.find_element_by_id("KSWUSER")
    passfield = driver.find_element_by_id("PWD")
    # enter creds, hit enter
    userfield.send_keys(krousr)
    passfield.send_keys(kropass)
    passfield.send_keys(Keys.ENTER)
    print("Entering credentials...")
    # check for existing session in progress
    time.sleep(3)
    try: driver.find_element_by_id("btnContinue").click()
    except: pass
    # get to eschedule portal
    driver.find_element_by_id("mySchedule").click()
    time.sleep(3) # wait for schedule to load
    driver.find_element_by_id("selfServ").click()
    # make soup out of page html
    html = driver.page_source
    print("Generating soup...")
    soup = BeautifulSoup(html,features="lxml")
    return soup

if __name__ == "__main__": getScheduleSoup()
