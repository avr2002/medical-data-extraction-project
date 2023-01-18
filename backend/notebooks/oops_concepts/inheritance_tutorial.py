import datetime


class Player:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_age(self) -> int:
        curr_date = datetime.datetime.now()
        age = curr_date.year - self.birth_year
        return age


class CricketPlayer(Player):
    def __init__(self, first_name, last_name, birth_year, team):
        Player.__init__(self, first_name, last_name, birth_year)
        self.team = team
        self.scores = []

    def add_score(self, score):
        if len(self.scores) == 0:
            self.scores.extend(score)
        else:
            self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is a cricket player from {self.team}."


class TennisPlayer(Player):
    def __init__(self, first_name, last_name, birth_year, grand_slam_winner):
        super().__init__(first_name, last_name, birth_year)
        self.grand_slam_winner = grand_slam_winner
        self.aces = []

    def get_avg_aces_per_match(self):
        return sum(self.aces) / len(self.aces)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is a Tennis Player."


virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
virat.add_score([80, 100, 0, 10])
virat.add_score(150)

print(virat)
print("Age:", virat.get_age())
print(virat.scores)
print(virat.get_avg_score())

roger = TennisPlayer('Roger', 'Federer', 1981, 20)

print(roger)
print("Age:", roger.get_age())
