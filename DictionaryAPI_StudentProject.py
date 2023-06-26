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
import pandas

app = Flask(__name__)
# If you import this file into another file, __name__ is dynamically replaced by this filename, i.e. main

@app.route("/")
def home():
    return render_template("dictionaryhome.html")


@app.route("/api/v1/<word>")
def dict_call(word):

    output = f'''{{"definition": {word.upper()},<br>
              {"&nbsp"*10}"word": {word}}}'''
    # boo that was so confusing and it wasn't even right haha

    result_dictionary = {"definition": word.upper(), "word": word}
    print(result_dictionary)
    return result_dictionary

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # default port is 5000. If you want to run two apps locally at the same time to check ur development,
    # specify a different port for each app.
