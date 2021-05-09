import datetime 
from pymongo import MongoClient
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    client = MongoClient("localhost", 27017)
    app.db = client.microblog
    entries = []

    @app.route("/", methods= ["GET", "POST"])
    def index(): 
        if request.method == "POST":
            entryContent = request.form.get("content")
            formatedDate = datetime.datetime.today().strftime("%Y-%m-%d")
            # entries.append((entryContent, formatedDate))
            app.db.entries.insert_one({"content": entryContent, 
                                        "date": formatedDate})

        # Format date the same way as it's represented on the web page.
        formatedEntries = [
            (
            entry["content"],
            entry["date"], 
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})]


            

        return render_template("index.html", entries = formatedEntries)
    return app