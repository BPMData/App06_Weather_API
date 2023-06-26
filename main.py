from flask import Flask, render_template
import pandas

app = Flask(__name__)
# If you import this file into another file, __name__ is dynamically replaced by this filename, i.e. main

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # df = pandas.read_csv("data.csv")
    # temperature = df.station(date)
    temperature = 23
    # return str(temperature)
    return{"station": station,
           "date": date,
           "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)
else:
    pass