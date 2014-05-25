'''
Created on May 25, 2014

@author: jerzy
'''
import unittest
import nussinov
import datetime

class IsOddTests(unittest.TestCase):
    """
     example tests of IsOdd fucntion from nussinov.py module
    """
    def testOne(self):
        self.failUnless(nussinov.IsOdd(1))

    def testTwo(self):
        self.failIf(nussinov.IsOdd(2))
        
class DatePatternTests(unittest.TestCase):
    """
     example tests of DatePattern class from nussinov.py module
    """
    def testMatches(self):
        p = nussinov.DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))
        
    def testMatchesYearAsWildCard(self):
        p = nussinov.DatePattern(0, 4, 10)
        d = datetime.date(2005, 4, 10)
        self.failUnless(p.matches(d))
        
    def testMatchesYearAndMonthAsWildCards(self):
        p = nussinov.DatePattern(0, 0, 1)
        d = datetime.date(2004, 10, 1)
        self.failUnless(p.matches(d))
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()