from flask import Flask, render_template, request
from games import Team, Game
import random
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    games = []
    if "cricketScores" in request.form:
        games = get_cricket_scores()
    elif "footballScores" in request.form:
        games = get_football_scores()
    return render_template("scores.jinja", games=games, ip=os.environ.get("POD_IP"))

def get_cricket_scores():
    teams = ["Sri Lanka", "Australia", "England", "India"]
    completed_scores = ["170/6, 20 Overs", "152/8, 20 Overs", "120 all out, 18.2 Overs", "201/4, 20 Overs"] 
    ongoing_scores = ["58/2, 6.2 Overs", "95/4, 14.5 Overs", "85/4, 17.5 Overs", "70/1, 8.4 Overs"]

    games = []
    picked_teams = []
    for  i in range(random.randint(1, 2)):
        while True:
            t1, t2 = random.sample(list(range(len(teams))), 2)
            if t1 not in picked_teams and t2 not in picked_teams:
                picked_teams.extend([t1, t2])
                break

        team1 = Team(teams[t1], completed_scores[t1])
        team2 = Team(teams[t2], ongoing_scores[t2])
        games.append(Game(team1, team2))
    
    return games


def get_football_scores():
    teams = ["Argentina", "Australia", "England", "Brazil"]
    scores = ["0", "1", "2", "3", "4"] 

    games = []
    picked_teams = []
    for  i in range(random.randint(1, 2)):
        while True:
            t1, t2 = random.sample(list(range(len(teams))), 2)
            if t1 not in picked_teams and t2 not in picked_teams:
                picked_teams.extend([t1, t2])
                break

        team1 = Team(teams[t1], scores[t1])
        team2 = Team(teams[t2], scores[t2])
        games.append(Game(team1, team2))
    
    return games