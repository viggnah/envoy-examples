from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/get-football-scores", methods=['GET'])
def get_football_scores():
    teams = ["Argentina", "Australia", "England", "Brazil"]
    scores = ["0", "1", "2", "3", "4"] 

    games = []
    picked_indexes = []
    for _ in range(random.randint(1, 2)):
        t1_index, t2_index = pick_random_nos_without_replacement(picked_indexes, teams)
        picked_indexes.extend([t1_index, t2_index])

        game = {
            "team1": {
                "name": teams[t1_index],
                "score": scores[t1_index]
            },
            "team2": {
                "name": teams[t2_index],
                "score": scores[t2_index]
            }
        }
        games.append(game)
    
    return jsonify(games)

def pick_random_nos_without_replacement(picked_indexes, teams):
    while True:
        t1_index, t2_index = random.sample(list(range(len(teams))), 2)
        if t1_index not in picked_indexes and t2_index not in picked_indexes:
            break
    return t1_index, t2_index

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6200)