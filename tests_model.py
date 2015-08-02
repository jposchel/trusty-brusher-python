#!/usr/bin/env python

"""tests_model.py: Tests for the model of the educational game Trusty Brusher."""

import sys
from tooth import Tooth
from germ import Germ
from food import Food
from person import Person

def test_tooth_class():
    """
       First, test Tooth class.
    
    """
    try:
        tooth_1 = Tooth(1, False, 0)
        assert tooth_1.get_location() == 1
        assert tooth_1.get_cavity_status() == False
        assert tooth_1.get_germ_count() == 0

        tooth_1.set_location(21)
        tooth_1.set_cavity_status(True)
        tooth_1.set_germ_count(10)
        assert tooth_1.get_location() == 21
        assert tooth_1.get_cavity_status() == True
        assert tooth_1.get_germ_count() == 10

        print("All Tooth class tests pass!")
    except:
        e = sys.exc_info()[0]
        print("Caught an error: %s" % e)

def test_germ_class():
    """
       Test Germ class.

    """
    try:
        germ_1 = Germ(52, 10)
        assert germ_1.get_location() == 52
        assert germ_1.get_health() == 10
        
        germ_1.set_location(103)
        germ_1.set_health(2)
        assert germ_1.get_location() == 103
        assert germ_1.get_health() == 2

        germ_1.increment_health()
        assert germ_1.get_health() == 3

        germ_1.decrement_health()
        germ_1.decrement_health()
        germ_1.decrement_health()
        assert germ_1.get_health() == 0

        germ_1.decrement_health()
        assert germ_1.get_health() == 0

        print("All Germ class tests pass!")
    except:
        e = sys.exc_info()[0]
        print("Caught an error: %s" % e)

def test_food_class():
    """
       Test Food class.

    """
    try:
        ice_cream_cone = Food("ice cream cone", 10, 1)
        assert ice_cream_cone.get_food_type() == "ice cream cone"
        assert ice_cream_cone.get_decay_value() == 10
        assert ice_cream_cone.get_cleaning_value() == 1

        ice_cream_cone.set_food_type("strawberry ice cream cone")
        assert ice_cream_cone.get_food_type() == "strawberry ice cream cone"

        carrot = Food("carrot", 2, 10)
        carrot.set_decay_value(1)
        carrot.set_cleaning_value(15)
        assert carrot.get_decay_value() == 1
        assert carrot.get_cleaning_value() == 15

        print("All Food class tests pass!")
    except:
        e = sys.exc_info()[0]
        print("Caught an error: %s" % e)

def test_person_class():
    """
       Test Person class.

    """
    try:
        Bobby = Person("Bobby", "Male")
        assert Bobby.get_name() == "Bobby"
        assert Bobby.get_gender() == "Male"

        print("All Person class tests pass!")
    except:
        e = sys.exc_info()[0]
        print("Caught an error: %s" % e)

def main():
    test_tooth_class()
    test_germ_class()
    test_food_class()
    test_person_class()

if __name__ =='__main__':
    main()


