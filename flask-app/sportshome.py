from flask import Flask, render_template, request
from games import Team, Game
import random
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def live_sports_scores():
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
    picked_indexes = []
    for _ in range(random.randint(1, 2)):
        t1_index, t2_index = pick_random_nos_without_replacement(picked_indexes, teams)
        picked_indexes.extend([t1_index, t2_index])

        team1 = Team(teams[t1_index], completed_scores[t1_index])
        team2 = Team(teams[t2_index], ongoing_scores[t2_index])
        games.append(Game(team1, team2))

    return games

def pick_random_nos_without_replacement(picked_indexes, teams):
    while True:
        t1_index, t2_index = random.sample(list(range(len(teams))), 2)
        if t1_index not in picked_indexes and t2_index not in picked_indexes:
            break
    return t1_index, t2_index

def get_football_scores():
    teams = ["Argentina", "Australia", "England", "Brazil"]
    scores = ["0", "1", "2", "3", "4"] 

    games = []
    picked_indexes = []
    for _ in range(random.randint(1, 2)):
        t1_index, t2_index = pick_random_nos_without_replacement(picked_indexes, teams)
        picked_indexes.extend([t1_index, t2_index])

        team1 = Team(teams[t1_index], scores[t1_index])
        team2 = Team(teams[t2_index], scores[t2_index])
        games.append(Game(team1, team2))
    
    return games

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5200)