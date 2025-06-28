from fileinput import filename

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/weather/")
def weather():
    return render_template("weather.html")


@app.route("/api/v1/<station>/<date>")
def weatherapi(station, date):
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temprature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"station": station, "date": date, "temperature": temprature}


@app.route("/api/v1/<params>")
def pillow(params):

    definition = ""
    if params == "pillow":
        definition = "Cushion place under the head for sleeping"
    elif params == "sun":
        definition = "The star at the center of our solar system"
    return {"definition": definition.upper(), "word": params}


if __name__ == "__main__":
    app.run(debug=True)