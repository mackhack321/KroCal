import json
hoursjson = json.load(open("hours.json"))
year = "2018"
timezone = "America/Chicago"
for date in hoursjson.keys():
    month = date.split("/")[0]
    day = date.split("/")[1]
    try:
        start = hoursjson[date].split(" - ")[0]
        end = hoursjson[date].split(" - ")[1]
        starthour = start.split(":")[0]
        startminute = start.split(":")[1]
        try:
            for char in startminute:
                if char.isalpha():
                    startminute.replace(char,"")
        except:
            pass
        print(f"{year}-{month}-{day}T{starthour}:{startminute}")
    except IndexError:
        pass
