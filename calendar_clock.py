#!/usr/bin/env python

"""calendar_clock.py: Public Calendar Clock class representing a time in the educational game Trusty Brusher."""

import threading
import time

class Calendar_Clock(threading.Thread):
    def __init__(self, init_start_day="Sunday", init_start_hour=7, init_start_minute=0):
    	threading.Thread.__init__(self)
        self.day_list = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
        self.current_day = init_start_day
        self.current_hour = init_start_hour
        self.current_minute = init_start_minute

