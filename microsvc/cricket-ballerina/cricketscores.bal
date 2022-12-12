import ballerina/random;
import ballerina/http;

configurable int port = 7200;

service / on new http:Listener(port) {

    resource function get get_cricket_scores () returns json[]|error {
        string[] teams = ["Sri Lanka", "Australia", "England", "India"];
        string[] completed_scores = ["170/6, 20 Overs", "152/8, 20 Overs", "120 all out, 18.2 Overs", "201/4, 20 Overs"];
        string[] ongoing_scores = ["58/2, 6.2 Overs", "95/4, 14.5 Overs", "85/4, 17.5 Overs", "70/1, 8.4 Overs"];

        json[] games = [];
        int[] picked_indexes = [];
        foreach int _ in 0 ..< (check random:createIntInRange(1, 3)) {
            int[2] [t1_index, t2_index] = check pick_random_nos_without_replacement(picked_indexes, teams);
            picked_indexes.push(t1_index, t2_index);

            json game = {
                "team1": {
                    "name": teams[t1_index],
                    "score": completed_scores[t1_index]
                },
                "team2": {
                    "name": teams[t2_index],
                    "score": ongoing_scores[t2_index]
                }
            };
            games.push(game);
        }
        
        return games;
    }
}

function pick_random_nos_without_replacement(int[] picked_indexes, string[] teams) returns int[2]|error {
    while true {
        int t1_index = check random:createIntInRange(0, teams.length());
        int t2_index = check random:createIntInRange(0, teams.length());

        if picked_indexes.indexOf(t1_index) == () && picked_indexes.indexOf(t2_index) == () {
            return [t1_index, t2_index];
        }
    }
}