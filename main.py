from re import A
from alarm_clock import Alarm_Clock

my_alarm_clock = Alarm_Clock("No Alarm")
print(my_alarm_clock.current_time)
my_alarm_clock.set_current_time()
my_alarm_clock.toggle_alarm()
my_alarm_clock.set_alarm_time()