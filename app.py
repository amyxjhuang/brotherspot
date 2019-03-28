from flask import Flask, render_template
import brotherspot
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "this is a program"

@app.route("/spotted", methods= ['POST'])
def spotted():
    raw_text = request.form.get('text')
    text_array = re.findall(r'["“”‘’\'](.*?)["“”‘’\']', raw_text)
    if len(text_array) != 3:
        return 'The format is /spotted "[name]" "[location]" "[time]"'
    title, start, end = text_array
    return brotherspot.getInfo(text_array)



if __name__ == "__main__":
    app.run()
