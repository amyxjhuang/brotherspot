from flask import Flask, render_template
import requests
import json

url = "https://hooks.slack.com/services/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"
locations = ["blackwell", "unit 1", "unit 2", "unit 3",
            "crossroads", "cafe 3", "moffitt", "mainstacks",
            "dwinelle", "ucha", "gong cha", "sather lane",
            "kresge", "evans", "leconte", "asian ghetto",
            "stanley", "soda", "cory", "etcheverry",
            "tause", "rsf", "foothill", "upper sproul", "mlk",
            "eshelmann", "sproul", "lower sproul",
            "wheeler", "doe", "latimer", "trader joes",
            "etch", "esh", "cafe blue door", "gbc", "sdh",
            "edwards stadium", "daiso", "sharetea", "chipotle"]

brotherLoc = {}

def getInfo(userInput):
    # userInput = ["brother", "blackwell", "12:00"];
    name = userInput[0]
    loc = userInput[1]
    time = userInput[2]
    if loc in locations:
        brotherLoc[name] = [loc, time]
        output = "Added: " + name + " has been spotted at " + loc + " at " + str(time)
        # output = uName;
    else:
        # return notInLoc(uLoc)
        output = "Location is not in list"
    data = {"text": output}
    requests.post(url, data = json.dumps(data))
