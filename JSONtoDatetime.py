import json
import scheduleToSoup as schedsoup

def finalFormatting(var): # make the times look nice
    for char in var:
        if char.isalpha():
            var = var.replace(char,"")
    if len(list(var.split(":")[0])) < 2: var = f"0{var}"
    if int(var.split(":")[0]) < 9 and int(var) != 0:
        var = str(int(var)+12)
    if int(var.split(":")[0]) == 10:
        var = str(22)
    return var

def schedJSONToDT(fp): # given a filename, turn it into a formatted datetime
    hoursjson = json.load(open(fp))
    year = "2018"
    timezone = "America/Chicago"

    datesToAdd = {}

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
            finalstart = f"{year}-{month}-{day}T{starthour}:{startminute}:00"
            finalend = f"{year}-{month}-{day}T{endhour}:{endminute}:00"
            datesToAdd[finalstart] = finalend
        except IndexError:
            pass

    return datesToAdd

if __name__ == "__main__": schedJSONToDT("hours.json")
