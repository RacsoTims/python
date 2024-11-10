from random import randint

class Team(object):
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


class Poule(object):
    
    teams = []
    standing = {}
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        header = "Team\tPlayed\tWon\tDrawn\tLost\tPoints\n"
        stats = [(str(team) + "\t" + "\t".join(map(str, performance)) + "\n") for (team, performance) in self.standing.items()]
        return f"{self.name}\n" + header + "".join(stats)[0:-1]
    
    def sort_standing(self):
        sorted = {}
        temp = []
        teams = list(self.standing.keys())
        while teams:
            next = teams.pop()
            if len(temp) == 0:
                temp.append(next)
            else:
                relative_performance = 0
                for team in temp:
                    if self.standing[team][-1] > self.standing[next][-1]:
                        relative_performance += 1
                temp.insert(relative_performance, next)
        for team in temp:
            sorted[team] = self.standing[team]
        self.standing = sorted
        return sorted
    
    def add_team(self, name):
        self.teams.append(Team(name))
    
    def get_team(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team
    
    def plan_matches(self):
        planned_matches = []
        for i in range(len(self.teams)):
            for j in self.teams[i+1:]:
                planned_matches.append(((self.teams[i]).name, j.name))
        return planned_matches
    
    def start_poule(self):
        for team in self.teams:
            self.standing[team] = [0, 0, 0, 0, 0]  # (0) matches played, (1) matches won, (2) matches drawn, (3) matches lost, (4) points
    
    def set_played(self, team):
        self.standing[team][0] += 1
    
    def set_points(self, team):
        self.standing[team][4] = self.standing[team][1] * 3 + self.standing[team][2]
    
    def set_won(self, team_name):
        team = self.get_team(team_name)
        self.standing[team][1] += 1
        self.set_played(team)
        self.set_points(team)
    
    def set_drawn(self, team_name):
        team = self.get_team(team_name)
        self.standing[team][2] += 1
        self.set_played(team)
        self.set_points(team)
    
    def set_lost(self, team_name):
        team = self.get_team(team_name)
        self.standing[team][3] += 1
        self.set_played(team)
        self.set_points(team)
    
    def play_matches(self):
        matches = self.plan_matches()
        for match in matches:
            home = match[0]
            away = match[1]
            result = randint(0, 2)
            if result == 0:
                self.set_won(home)
                self.set_lost(away)
            elif result == 1:
                self.set_drawn(home)
                self.set_drawn(away)
            else:
                self.set_lost(home)
                self.set_won(away)
        return True


# class Match(object):
    
#     def __init__(self, home, away):
#         self.home = home
#         self.away = away
    
#     def result(self):
#         pass


poule = Poule("Poule0")

poule.add_team("A")
poule.add_team("B")
poule.add_team("C")
poule.add_team("D")

poule.start_poule()
if poule.play_matches():
    poule.sort_standing()
    print(poule)
