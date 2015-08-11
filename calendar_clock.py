#!/usr/bin/env python

"""calendar_clock.py: Public Calendar Clock class representing a time in the educational game Trusty Brusher."""

import threading
import time

class Calendar_Clock(threading.Thread):
    """
       A Calendar Clock that tracks current day of the week, current hour, and current minute.
       self.day_list: list value indicating names and order of days of the week
       self.current_day: string value indicating the current day of the week
       self.current_hour: int value indicating the current hour of the day (24-hour clock is used, 0-23)
       self.current_minute: int value indicating the current minute of the hour (60 minutes per hour, 0-59)
       self.stop_clock_flag: bool value indicating whether or not the Calendar Clock should stop

       To use Calendar_Clock, create an instance and call Python threading module methods on that instance:

           some_new_clock = Calendar_Clock()
           # ... or ...
           some_new_clock = Calendar_Clock("Friday", 17, 5)

           some_new_clock.start()
           
           # ... do some work ...
           # ... use instance methods defined below ...
           # ... and when finished ...

           some_new_clock.stop()
           some_new_clock.join()

       Some class design elements taken from Python Advanced Turtorial 5 - MultiThreading
       by DrapsTV, found here: https://youtu.be/EvbA3qVMGaw

    """
    def __init__(self, init_start_day="SUNDAY", init_start_hour=7, init_start_minute=0):
        threading.Thread.__init__(self)
        self.stop_clock_flag = False
        self.day_list = [ "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY" ]
        self.current_day = init_start_day
        self.current_day = self.current_day.upper()
        self.current_hour = init_start_hour
        self.current_minute = init_start_minute

    def run(self):
        while self.stop_clock_flag == False:
            #self.day_list.index(self.current_day)
            time.sleep(0.5)

    def stop(self):
        self.stop_clock_flag = True

    def get_day(self):
        return self.current_day

    def set_day(self, new_day):
        self.current_day = new_day
        self.current_day = self.current_day.upper()

    def get_hour(self):
        return self.current_hour

    def set_hour(self, new_hour):
        self.current_hour = new_hour

    def get_minute(self):
        return self.current_minute

    def set_minute(self, new_minute):
        self.current_minute = new_minute

    def get_time_stamp(self):
        if self.current_hour < 10:
    	    formated_hour = "0{}".format(str(self.current_hour))
        else:
            formated_hour = str(self.current_hour)
    	if self.current_minute < 10:
    	    formated_minute = "0{}".format(str(self.current_minute))
    	else:
    	    formated_minute = str(self.current_minute)
        return "{} {}:{}".format(self.current_day, formated_hour, formated_minute)
