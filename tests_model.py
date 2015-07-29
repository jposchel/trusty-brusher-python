#!/usr/bin/env python

"""tests_model.py: Tests for the model of the educational game Trusty Brusher."""

import sys
from tooth import Tooth

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

def main():
    test_tooth_class()

if __name__ =='__main__':
    main()


