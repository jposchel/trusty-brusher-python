#!/usr/bin/env python

"""person.py: Public Person class representing a person in the educational game Trusty Brusher."""

class Person:
	"""
       A Person who eats and needs dental care.
       self.name: string value indicating the person's name
       self.gender: string value indicating the person's gender
       self.is_awake: bool value indicating whether or not the person is awake
       self.is_sleeping: bool value indicating whether or not the person is sleeping
       self.is_eating: bool value indicating whether or not the person is eating
       self.is_hurting: bool value indicating whether or not the person is hurting
       self.is_brushing: bool value indicating whether or not the person is brushing their teeth
       self.is_flossing: bool value indicating whether or not the person is flossing their teeth

    """
    def __init__(self, init_name, init_gender):
    	self.name = init_name
    	self.gender = init_gender
    	self.is_awake = True
    	self.is_sleeping = False
    	self.is_eating = False
    	self.is_hurting = False
    	self.is_brushing = False
    	self.is_flossing = False
    
    def __change_person_states(self, awake_state, sleeping_state, eating_state,
      hurting_state, brushing_state, flossing_state):
        self.is_awake = awake_state
        self.is_sleeping = sleeping_state
        self.is_eating = eating_state
        self.is_hurting = hurting_state
        self.is_brushing = brushing_state
        self.is_flossing = flossing_state
    
    def be_alert(self):


    def wake_up(self):

    def go_to_sleep(self):

    def eat(self):

    def hurt(self):

    def brush_teeth(self):

    def floss_teeth(self):

    def get_name(self):

    def set_name(self, new_name):

    def get_gender(self):

    def set_gender(self, new_gender):

    def get_is_awake(self):

    def toggle_awake(self):

    def get_is_sleeping(self):

    def toggle_sleeping(self):

    def get_is_eating(self):

    def toggle_eating(self):

    def get_is_hurting(self):

    def toggle_hurting(self):

    def get_is_brushing(self):

    def toggle_brushing(self):

    def get_is_flossing(self):

    def toggle_flossing(self):
    
