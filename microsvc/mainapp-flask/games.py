class Game:
    def __init__(self, team1, team2) -> None:
        self.team1 = team1
        self.team2 = team2
    
class Team:
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score