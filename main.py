from alarm_clock import Alarm_Clock

my_alarm_clock = Alarm_Clock("1139", False, "No Alarm")
print(my_alarm_clock.current_time)
my_alarm_clock.set_current_time("1200")
my_alarm_clock.toggle_alarm()
