from flask import Flask, render_template

app = Flask(__name__)
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
@app.route("/")
def index():
    userInput = ["brother", "blackwell", 1200];
    uName = userInput[0]
    uLoc = userInput[1]
    uTime = userInput[2]
    if uLoc in locations:
        brotherLoc[uName] = [uLoc, uTime]
        return "Added: " + uName + " has been spotted at " +
                uLoc + " at " + str(uTime)
    else:
        return notInLoc(uLoc)


def notInLoc(str s):
    return "location is not in list"

if __name__ == "__main__":
    app.run()
