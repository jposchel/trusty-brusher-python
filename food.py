#!/usr/bin/env python

"""food.py: Public Food class representing food entities in the educational game Trusty Brusher."""

class Food:
    """
       A Food eaten by a Person.
       self.food_type: string value indicating type of food
       self.decay_value: int value indicating propensity of food to cause tooth decay
           Higher value indicates higher propensity; lower value indicates lower propensity
       self.cleaning_value: int value indicating propensity of food to prevent tooth decay
           Higher value indicates higher propensity; lower value indicates lower propensity

    """
    def __init__(self, init_food_type, init_decay_value, init_cleaning_value):
        self.food_type = init_food_type
        self.decay_value = init_decay_value
        self.cleaning_value = init_cleaning_value

    def get_food_type(self):
        return self.food_type

    def set_food_type(self, new_food_type):
        self.food_type = new_food_type

    def get_decay_value(self):
        return self.decay_value

    def set_decay_value(self, new_decay_value):
        self.decay_value = new_decay_value

    def get_cleaning_value(self):
        return self.cleaning_value

    def set_cleaning_value(self, new_cleaning_value):
        self.cleaning_value = new_cleaning_value

