from flask import Flask, request, render_template, make_response, redirect
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("games.html")

@app.route("/get_dlcs/<game_id>")
def game_dlcs_page(game_id):
    return render_template("dlcs.html", game_id=game_id, game_name="Teste")

if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)
