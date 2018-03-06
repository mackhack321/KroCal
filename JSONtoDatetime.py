import json

def finalFormatting(var):
    for char in var:
        if char.isalpha():
            var = var.replace(char,"")
    if len(list(var.split(":")[0])) < 2: var = f"0{var}"
    return var

def schedJSONToDT(fp):
    hoursjson = json.load(open(fp))
    year = "2018"
    timezone = "America/Chicago"

    datesToAdd = {}

    print("7:30")
    print(finalFormatting("7:30"))
    print("1:30")
    print(finalFormatting("1:30"))
    for date in hoursjson.keys():
        month = date.split("/")[0]
        day = date.split("/")[1]
        try:
            # 2014-04-10T00:00:00.000
            starttime = hoursjson[date].split(" - ")[0]
            endtime = hoursjson[date].split(" - ")[1]
            starthour = finalFormatting(starttime.split(":")[0])
            startminute = finalFormatting(starttime.split(":")[1])
            endhour = finalFormatting(endtime.split(":")[0])
            endminute = finalFormatting(endtime.split(":")[1])
            finalstart = f"{year}-{month}-{day}T{starthour}:{startminute}:00-06:00"
            finalend = f"{year}-{month}-{day}T{endhour}:{endminute}:00-06:00"
            print(finalstart,finalend)
        except IndexError:
            pass

if __name__ == "__main__": schedJSONToDT("hours.json")
