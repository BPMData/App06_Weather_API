from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
# If you import this file into another file, __name__ is dynamically replaced by this filename, i.e. main

stations = pd.read_csv("datafiles/data_small/stations.txt", skiprows=17)
stations = stations.iloc[:,[0,1]]

@app.route("/")
def home():
   return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    filename = "datafiles/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return{"station": station,
           "date": date,
           "temperature in C": temperature}

@app.route("/api/v1/<station>/")
def all_data(station):
    filename = "datafiles/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

"""
Note we can re-use variable names like filename, df and station because we 
only ever defined these as LOCAL variables within particular functions.
"""

@app.route("/api/v1/annual/<station>/<year>")
def yearly(station, year):
    filename = "datafiles/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))]
    result = df.to_dict(orient="records")
    # You could use the code:
    # result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    # But that looks a little ridiculous IMO.

    return result



if __name__ == "__main__":
    app.run(debug=True)
    # default port is 5000. If you want to run two apps locally at the same time to check ur development,
    # specify a different port for each app.
else:
    pass