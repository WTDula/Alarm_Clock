import datetime

class Alarm_Clock:
    def __init__(self, alarm_time):
        self.current_time = datetime.datetime.now()
        self.alarm_is_on = False
        self.alarm_time = alarm_time
        self.last_checked = self.current_time

    def set_current_time(self):
        self.current_time = input("What time is it? ")
        print(f"The current time is {self.current_time}.")

    def toggle_alarm(self):
        self.alarm_is_on = not(self.alarm_is_on)
        if(self.alarm_is_on):
            print("The alarm is armed.")
        else:
            print("The alarm has been disarmed.")

    def set_alarm_time(self):
        self.alarm_time = input("What time do you want the alarm set to? ")
        if(self.alarm_is_on == False):
            self.alarm_is_on = True
        print(f"The current alarm time is {self.alarm_time}")

    def ticks_since_last_checked(self):
        self.last_checked = datetime.datetime.now()
        ticks = self.last_checked - self.current_time
        ticks = round(ticks.total_seconds())
        print(f"The clock has ticked {ticks} times since you last checked.")

    def trigger_alarm(self):
        pass