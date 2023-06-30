"""
desired ability:
if you go to http://127.0.0.1:5000/api/v1/<word>
you should get a dictionary that consists of:

{
"definition": <definition_of_word>,
"word": <word>
}

"""

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
# If you import this file into another file, __name__ is dynamically replaced by this filename, i.e. main

dict = pd.read_csv("datafiles/dictionary.csv")


@app.route("/")
def home():
    return render_template("dictionaryhome.html")


@app.route("/api/v1/<input>")
def finder(input):
    # dict = pd.read_csv("datafiles/dictionary.csv") - by putting this inside the function,
    # it runs every time you go to a new word url.
    # NBD locally and for a small csv, but would be bad on a server with a large csv.
    # so it goes outside the fn.
    # Unless you wanted to call the CSV every time because maybe the CSV gets updated...
    input = input.casefold()
    output = dict.loc[dict["word"] == input]["definition"].squeeze()
    return {"definition": output, "word": input}
    # output = eval('f"""{output}"""')
    # This was dumb to attempt, I don't think you an get the text to show with line breaks properly INSIDE the dictionary itself, anyway.
    # See test.py for why this won't work.

    # output = f'''{{"definition": {word.upper()},<br>
    #           {"&nbsp"*10}"word": {word}}}'''
    # boo that was so confusing and it wasn't even right haha

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # default port is 5000. If you want to run two apps locally at the same time to check ur development,
    # specify a different port for each app.



