import datetime 
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route("/", methods= ["POST", "GET"])
def index(): 
    if request.method == "POST":
        entryContent = request.form.get("content")
        formatedDate = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entryContent, formatedDate))

# Format date properly
        formatedEntries = [(entry[0],
                            entry[1], 
                            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d"))
                            for entry in entries]

    return render_template("index.html", entries = formatedEntries)