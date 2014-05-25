'''
Created on May 25, 2014

@author: jerzy
'''
import unittest
import nussinov


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(nussinov.IsOdd(1))

    def testTwo(self):
        self.failIf(nussinov.IsOdd(2))
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()