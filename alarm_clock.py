class Alarm_Clock:
    def __init__(self, current_time, alarm_is_on, alarm_time):
        self.current_time = current_time
        self.alarm_is_on = alarm_is_on
        self.alarm_time = alarm_time

    def set_current_time(self, time):
        self.current_time = time
        print(f"The current time is {self.current_time}.")

    def toggle_alarm(self):
        self.alarm_is_on = not(self.alarm_is_on)
        if(self.alarm_is_on):
            print("The alarm is armed.")
        else:
            print("The alarm has been disarmed.")

    def set_alarm_time(self, time):
        self.alarm_time = time
        print(f"The current alarm time is {self.alarm_time}")

        
