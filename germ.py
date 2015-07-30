#!/usr/bin/env python

"""germ.py: Public Germ class representing germ entities in the educational game Trusty Brusher."""

class Germ:
    """
       A Germ, often on a Tooth, in the Mouth of a Person.
       self.location: int value indicating location of Germ in the Mouth
       self.health: int value indicating the current health of Germ
    
    """

    def __init__(self, init_location, init_health):
        self.location = init_location
        self.health = init_health

    def get_location(self):
        return self.location

    def set_location(self, new_location):
        self.location = new_location

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def increment_health(self):
        self.health = self.health + 1

    def decrement_health(self):
        if self.health > 0:
            self.health = self.health - 1


