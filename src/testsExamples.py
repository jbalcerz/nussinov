'''
Created on May 25, 2014

@author: jerzy
@brief: 

just some examples how to use unit tests
'''
import unittest
import datetime


def IsOdd(n):
    """
     function just to play with unit tests
    """
    return n % 2 == 1


class DatePattern:
    """    
     class just to play with unit tests
    """
    def __init__(self, year, month, day):
        self.year  = year
        self.month = month
        self.day   = day
    
    def matches(self, date):
        return ((self.year  and self.year  == date.year  or True) and
                (self.month and self.month == date.month or True) and
                self.day == date.day)

"""
************EXAMPLE TESTS*******************************************************
"""

class IsOddTests(unittest.TestCase):
    """
     example tests of IsOdd fucntion from main.py module
    """
    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))
        
class DatePatternTests(unittest.TestCase):
    """
     example tests of DatePattern class from main.py module
    """
    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))
        
    def testMatchesYearAsWildCard(self):
        p = DatePattern(0, 4, 10)
        d = datetime.date(2005, 4, 10)
        self.failUnless(p.matches(d))
        
    def testMatchesYearAndMonthAsWildCards(self):
        p = DatePattern(0, 0, 1)
        d = datetime.date(2004, 10, 1)
        self.failUnless(p.matches(d))
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
