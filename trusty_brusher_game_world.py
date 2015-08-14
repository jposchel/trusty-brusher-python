#!/usr/bin/env python

"""trusty_brusher_game_world.py: Public Game World class representing the educational game Trusty Brusher."""

from calendar_clock import Calendar_Clock
from food import Food
from germ import Germ
from person import Person
from tooth import Tooth

class Trusty_Brusher_Game_World:
    def __init__(self, init_person_name, init_person_gender, healthy_food_info, unhealthy_food_info):
        self.master_clock = Calendar_Clock()
        self.main_person = Person(init_person_name, init_person_gender)
        self.teeth = [Tooth(counter, False, 0) for counter in range(26)]
        self.healthy_food = [Food(specs[0], specs[1], specs[2]) for specs in healthy_food_info]
        self.unhealthy_food = [Food(specs[0], specs[1], specs[2]) for specs in unhealthy_food_info]
        self.upcoming_food = []
        self.tooth_brush = False
        self.tooth_paste = False
        self.floss = False
        self.game_over = False
        self.game_paused = False
