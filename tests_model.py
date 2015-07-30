#!/usr/bin/env python

"""tests_model.py: Tests for the model of the educational game Trusty Brusher."""

import sys
from tooth import Tooth
from germ import Germ

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

def main():
    test_tooth_class()
    test_germ_class()

if __name__ =='__main__':
    main()


