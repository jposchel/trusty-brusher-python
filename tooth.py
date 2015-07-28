#!/usr/bin/env python

"""Tooth.py: Public Tooth class representing tooth entities in the educational game Trusty Brusher."""

class Tooth:
    """
       A Tooth in the Mouth of a Person.
       self.location: int value indicating location of Tooth in the Mouth
       self.has_cavity: bool value indicating whether or not the Tooth has a cavity
       self.new_germ_count: int value indicating number of germs that currently rest on the Tooth
    
    """
    
    def __init__(self, new_location, new_cavity_status, new_germ_count):
        self.location = new_location
        self.has_cavity = new_cavity_status
        self.germ_count = new_germ_count

    def get_location(self):
        return self.location

    def set_location(self, new_loc):
        self.location = new_loc

    def get_cavity_status(self):
        return self.has_cavity

    def set_cavity_status(self, new_status):
        self.has_cavity = new_status

    def get_germ_count(self):
        return self.germ_count

    def set_germ_count(self, new_count):
        self.germ_count = new_count


