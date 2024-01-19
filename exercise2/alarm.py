class Alarm:
    
    def __init__(self):
        self.current_time = {'hour':0, 'minutes':0, 'seconds':0}
        self.alarm_time  = {'hour':0, 'minutes':0}
        self.alarmed = False
        
    
    def set_alarm_time(self, hour, minutes):
        self.alarm_time['hour'] = int(hour)
        self.alarm_time['minutes'] = int(minutes)
        print("Thank you, alarm was set up, and you wouldn't miss your lecture")
        
        
    def change_time(self, hour, minutes, seconds):
        self.current_time['hour'] = int(hour)
        self.current_time['minutes'] = int(minutes)
        self.current_time['seconds'] = int(seconds)
        self.display_current_time()
        
    def display_current_time(self):
        print(f"Current time is - {self.current_time['hour']}:{self.current_time['minutes']}:{self.current_time['seconds']} ")
        
    def check_clock_alarmed(self):
        return self.alarmed
    
    def time_increase(self):
        self.current_time['seconds'] += 1
        if self.current_time['seconds'] == 60:
            self.current_time['minutes'] += 1
            self.current_time['seconds'] = 0
            if self.current_time['minutes'] == 60:
                self.current_time['hour'] += 1
                self.current_time['minutes'] = 0
                if self.current_time['hour'] == 24:
                    self.current_time['hour'] = 0
        self.display_current_time()
        
    
    def alarming(self):
        if ((self.current_time['hour'] == self.alarm_time['hour']) & (self.current_time['minutes'] == self.alarm_time['minutes'])):
            self.alarmed = True
            print('AAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLAAAAAAAAAAAARRRRRRRRMMMMMMMMMM!!!!!!!!!!!!!!!!')


def main():
    alarm = Alarm()
    time = input('Please insert current time : ')
    alarm.change_time(time.split(':')[0], time.split(':')[1], time.split(':')[2])
    time = input('Please insert time of alarm : ')
    alarm.set_alarm_time(time.split(':')[0], time.split(':')[1])
    
    while not(alarm.check_clock_alarmed()):
        alarm.time_increase()
        alarm.alarming()
    
main()