#!/usr/bin/env python

"""trusty_brusher_game_world.py: Public Game World class representing the educational game Trusty Brusher."""

from calendar_clock import Calendar_Clock
from food import Food
from germ import Germ
from person import Person
from tooth import Tooth

class Trusty_Brusher_Game_World:
    def __init__(self, init_person_name, init_person_gender):
        self.master_clock = Calendar_Clock()
        self.main_person = Person(init_person_name, init_person_gender)
        for counter in range(26):
            self.tooth[].append(Tooth(counter, False, 0))

