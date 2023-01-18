import datetime

class CricketPlayer:
    def __init__(self, first_name: str, last_name: str, birth_year: int, team: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def get_age(self) -> int:
        curr_date = datetime.datetime.now()
        age = curr_date.year - self.birth_year
        return age

    def add_score(self, score):
        if len(self.scores) == 0:
            self.scores.extend(score)
        else:
            self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores) / len(self.scores)

    def __lt__(self, other):
        # Operator Overloading
        my_score = self.get_avg_score()
        other_score = other.get_avg_score()
        return my_score < other_score

    def __str__(self):
        return f"{self.first_name} {self.last_name} is a cricket player from {self.team}."





virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
virat.add_score([80, 100, 0, 10])
virat.add_score(150)

print(virat.get_age())
print(virat.scores)
print(virat.get_avg_score())

david = CricketPlayer('David', 'Warner', 1985, 'Australia')
print(david.first_name)
print(david.get_age())
david.add_score([100, 101, 98, 0, 1])

print(david.scores)
print(david.get_avg_score())

print(virat < david)

print(virat)
print(david)
