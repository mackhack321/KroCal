import mechanicalsoup as ms
from bs4 import BeautifulSoup as soup
import http.cookiejar as cookiejar
import json

krocreds = json.load(open("krologin.json")) # get greatpeople login
username = krocreds["login"]
password = krocreds["pass"]
base_url = "https://vpnb-cdc.kroger.com/EmpowerESS/,DanaInfo=myeschedule.kroger.com+Schedule.aspx"
br = ms.StatefulBrowser()

br.open(base_url)
print(br.get_url())
currentpage = br.get_current_page()
loginform = currentpage.find("form",{"class":"form-signin"})
br.select_form(loginform)
loginform["KSWUSER"] = username
loginform["PWD"] = password
br.submit_selected()


# allforms = br.get_current_page().find_all("form")
# loginform = br.find("form",{"class":"form-signin"})
# form = br.get_form(loginform)
# form["KSWUSER"] = username
# form["PWD"] = password
#
# br.submit_form(form)
# print(br.parsed())
