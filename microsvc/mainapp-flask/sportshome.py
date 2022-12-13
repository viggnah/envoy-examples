from flask import Flask, render_template, request
from games import Team, Game
import os
import requests

app = Flask(__name__)

FOOTBALL_SCORES_URL = os.environ.get("FOOTBALL_SCORES_URL")
CRICKET_SCORES_URL = os.environ.get("CRICKET_SCORES_URL")

@app.route("/", methods=['GET', 'POST'])
def live_sports_scores():
    games = []
    if "cricketScores" in request.form:
        games = get_cricket_scores()
    elif "footballScores" in request.form:
        games = get_football_scores()
    return render_template("scores.jinja", games=games, ip=os.environ.get("POD_IP"))

def get_cricket_scores():
    json_resp = requests.get(CRICKET_SCORES_URL).json()

    games = []
    for resp in json_resp:
        team1 = Team(resp.get("team1").get("name"), resp.get("team1").get("score"))
        team2 = Team(resp.get("team2").get("name"), resp.get("team2").get("score"))
        games.append(Game(team1, team2))
    
    return games

def get_football_scores():
    json_resp = requests.get(FOOTBALL_SCORES_URL).json()

    games = []
    for resp in json_resp:
        team1 = Team(resp.get("team1").get("name"), resp.get("team1").get("score"))
        team2 = Team(resp.get("team2").get("name"), resp.get("team2").get("score"))
        games.append(Game(team1, team2))
    
    return games

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5200)