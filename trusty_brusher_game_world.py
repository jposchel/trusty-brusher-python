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
        self.toothbrush = False
        self.toothpaste = False
        self.floss = False
        self.game_paused = False
        self.game_over = False

    def is_game_paused(self):
        return self.game_paused

    def pause_game(self, new_pause_status):
        self.game_paused = new_pause_status

    def is_game_over(self):
        return self.game_over

    def get_toothbrush_status(self):
        return self.toothbrush

    def set_toothbrush_status(self, new_brush_status):
        self.toothbrush = new_brush_status

    def get_toothpaste_status(self):
        return self.toothpaste

    def set_toothpaste_status(self, new_paste_status):
        self.toothpaste = new_paste_status

    def add_healthy_food(self, food_item_specs):
        self.healthy_food.extend(Food(food_item_specs[0], food_item_specs[1], food_item_specs[2]))
