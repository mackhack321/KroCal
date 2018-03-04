from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup
import http.cookiejar as cookiejar
import json

krocreds = json.load(open("krologin.json")) # get greatpeople login
username = krocreds["login"]
password = krocreds["pass"]
base_url = "https://vpnb-cdc.kroger.com/EmpowerESS/,DanaInfo=myeschedule.kroger.com+Schedule.aspx"
br = RoboBrowser(history=True,parser="lxml")

br.open(base_url)
allforms = br.find_all("form")
loginform = br.find("form",{"class":"form-signin"})
form = br.get_form(loginform)
form["KSWUSER"] = username
form["PWD"] = password
br.session.headers["Referer"] = base_url
br.submit_form(form)
print(br.parsed)
