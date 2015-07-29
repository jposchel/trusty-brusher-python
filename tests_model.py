#!/usr/bin/env python

"""tests_model.py: Tests for the model of the educational game Trusty Brusher."""

import sys

def test_tooth_class():
    """
       First, test Tooth class.
    
    """
    try:
        tooth_1 = Tooth(1, False, 0)
        print("All Tooth class tests pass!")
    except:
        e = sys.exc_info()[0]
        print("Caught an error: %s" % e)

def main():
    test_tooth_class()

if __name__ =='__main__':
    main()


