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
        self.current_food = None
        self.food_pointer = None
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

    def remove_healthy_food(self):
        if len(self.healthy_food) > 0:
            self.healthy_food.remove( self.healthy_food[ len(self.healthy_food - 1) ] )

    def add_unhealthy_food(self, food_item_specs):
        self.unhealthy_food.extend(Food(food_item_specs[0], food_item_specs[1], food_item_specs[2]))

    def remove_unhealthy_food(self):
        if len(self.unhealthy_food) > 0:
            self.unhealthy_food.remove( self.unhealthy_food[ len(self.unhealthy_food - 1) ] )

    def _advance_food(self):
        if self.food_pointer == None:
            self.current_food = self.healthy_food[0]
            self.food_pointer = [1, 0]
        elif self.food_pointer[0] == 0:
            self.current_food = self.unhealthy_food[self.food_pointer[1]]
            if self.food_pointer[1] == len(self.unhealthy_food) - 1:
                self.food_pointer = [1, 0]
            else:
                self.food_pointer = [1, self.food_pointer[1] + 1]
        elif self.current_food[0] == 1:
            self.current_food = self.healthy_food[self.food_pointer[1]]
            if self.food_pointer[1] == len(self.healthy_food) - 1:
                self.food_pointer = [0, 0]
            else:
                self.food_pointer = [0, self.food_pointer[1] + 1]

    def eat(self):
        # Put awesomeness here
        # Eat well
