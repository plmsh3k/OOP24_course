import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


class HockeyLeagueStatistics:
    def __init__(self, data):
        self.data = data

    def search_player(self, player_name):
        for player in self.data:
            if player['name'] == player_name:
                return player
        return None

    def list_team_abbreviations(self):
        team_abbreviations = sorted(set(player['team'] for player in self.data))
        return team_abbreviations

    def list_country_abbreviations(self):
        country_abbreviations = sorted(set(player['nationality'] for player in self.data))
        return country_abbreviations

    def list_players_in_team(self, team):
        team_players = [player for player in self.data if player['team'] == team]
        sorted_players = sorted(team_players, key=lambda x: x['goals'] + x['assists'], reverse=True)
        return sorted_players

    def list_players_from_country(self, country):
        country_players = [player for player in self.data if player['nationality'] == country]
        sorted_players = sorted(country_players, key=lambda x: x['goals'] + x['assists'], reverse=True)
        return sorted_players

    def list_most_points(self, n):
        sorted_players = sorted(self.data, key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)[:n]
        return sorted_players

    def list_most_goals(self, n):
        sorted_players = sorted(self.data, key=lambda x: (x['goals'], x['games']), reverse=True)[:n]
        return sorted_players

    def instructions(self):
            print("commands:")
            print("0 quit")
            print("1 search for player")
            print("2 teams")
            print("3 countries")
            print("4 players in team")
            print("5 players from country")
            print("6 most points")
            print("7 most goals")

    def run(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == '0':
                break
            elif command == '1':
                name = input("name: ")
                player = self.search_player(name)
                if player:
                    print(f"{player['name']:20} {player['team']:3} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")
                else:
                    print("Player not found.")
            elif command == '2':
                team_abbreviations = self.list_team_abbreviations()
                print(' '.join(team_abbreviations))
            elif command == '3':
                country_abbreviations = self.list_country_abbreviations()
                print(' '.join(country_abbreviations))
            elif command == '4':
                team = input("team: ")
                team_players = self.list_players_in_team(team)
                for player in team_players:
                    print(f"{player['name']:20} {player['team']:3} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")
            elif command == '5':
                country = input("country: ")
                country_players = self.list_players_from_country(country)
                for player in country_players:
                    print(f"{player['name']:20} {player['team']:3} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")
            elif command == '6':
                n = int(input("how many: "))
                most_points_players = self.list_most_points(n)
                for player in most_points_players:
                    print(f"{player['name']:20} {player['team']:3} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")
            elif command == '7':
                n = int(input("how many: "))
                most_goals_players = self.list_most_goals(n)
                for player in most_goals_players:
                    print(f"{player['name']:20} {player['team']:3} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")



if __name__ == "__main__":
    data = read_json_file("part.json")
    app = HockeyLeagueStatistics(data)
    app.run()