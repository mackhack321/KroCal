# Enter KroCal...
...a project that scrapes work schedule data from GreatPeople and adds it to your Google Calendar.

If you aren't a Kroger employee, you won't understand the struggle.

Requirements:
Libaries listed in requirements.txt, can be installed with 'pip install -r requirements.txt'
Google Chrome
A Google Calendar API Client ID file named "client_id.json"
A JSON file containing your GreatPeople login information named "krologin.json"

"krologin.json" should be structured as the following:
{
    "login": "YOUR_USERNAME"
    "pass": "YOUR_PASSWORD"
}

"client_id.json" should be structured exactly as Google gives it to you
