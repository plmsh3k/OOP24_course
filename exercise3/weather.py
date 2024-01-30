class WeatherStation:
    def __init__(self, name: str):
        self.name = name
        self.list_of_observations = []
        
    def add_observations(self, observation : str):
        self.list_of_observations.append(observation)
    
    def last_observations(self):
        return self.list_of_observations[-1]
    
    def number_of_observations(self):
        return len(self.list_of_observations)
    
    def __str__(self):
        return f"{self.name}, {self.number_of_observations()} observations"
    

if __name__ == '__main__':
    station = WeatherStation('Houston')
    station.add_observations('Rain 10mm')
    station.add_observations('Sunny')
    print(station.last_observations())
    
    station.add_observations('Thunderstorm')
    print(station.last_observations())
    
    print(station.number_of_observations())
    print(station)
    