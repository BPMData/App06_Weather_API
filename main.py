from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
# If you import this file into another file, __name__ is dynamically replaced by this filename, i.e. main

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "datafiles/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return{"station": station,
           "date": date,
           "temperature in C": temperature}

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # default port is 5000. If you want to run two apps locally at the same time to check ur development,
    # specify a different port for each app.
else:
    pass