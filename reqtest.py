import json
import requests
from lxml import html

jsondata = json.load(open("krologin.json"))
username = jsondata["login"]
password = jsondata["pass"]

payload = {"KSWUSER":username,"PWD":password}
session_requests = requests.session()
login_url = "http://greatpeople.me"
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
result = session_requests.post(login_url,data=payload,headers=dict(referer=login_url))

print(result.content)
