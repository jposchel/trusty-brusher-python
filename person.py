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
    
    def __change_action_states(self, awake_state, sleeping_state, eating_state,
      hurting_state, brushing_state, flossing_state):
        self.is_awake = awake_state
        self.is_sleeping = sleeping_state
        self.is_eating = eating_state
        self.is_hurting = hurting_state
        self.is_brushing = brushing_state
        self.is_flossing = flossing_state

    def be_alert(self):
        self.__change_action_states(True, False, False, False, False, False)

    def wake_up(self):
        self.be_alert()

    def go_to_sleep(self):
        self.__change_action_states(False, True, False, False, False, False)

    def eat(self):
        self.__change_action_states(True, False, True, False, False, False)

    def hurt(self):
        self.__change_action_states(True, False, False, True, False, False)

    def brush_teeth(self):
        self.__change_action_states(True, False, False, False, True, False)

    def floss_teeth(self):
        self.__change_action_states(True, False, False, False, False, True)

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_gender(self):
        return self.gender

    def get_is_awake(self):
        return self.is_awake

    def toggle_awake(self):
        if self.is_awake == True:
            self.is_awake = False
        else:
            self.is_awake = True

    def get_is_sleeping(self):
        return self.is_sleeping

    def toggle_sleeping(self):
        if self.is_sleeping == True:
            self.is_sleeping = False
        else:
            self.is_sleeping = True

    def get_is_eating(self):
        return self.is_eating

    def toggle_eating(self):
        if self.is_eating == True:
            self.is_eating = False
        else:
            self.is_eating = True

    def get_is_hurting(self):
        return self.is_hurting

    def toggle_hurting(self):
        if self.is_hurting == True:
            self.is_hurting = False
        else:
            self.is_hurting = True

    def get_is_brushing(self):
        return self.is_brushing

    def toggle_brushing(self):
        if self.is_brushing == True:
            self.is_brushing = False
        else:
            self.is_brushing = True

    def get_is_flossing(self):
        return self.is_flossing

    def toggle_flossing(self):
        if self.is_flossing == True:
            self.is_flossing = False
        else:
            self.is_flossing = True
    
