'''
Created on May 26, 2014

@author: jerzy
'''
import unittest
import nussinov
from numpy import matrix


testChain1 = 'GGGAAAACCC'
testEnergyMatrix = 

class NussinovTests(unittest.TestCase):
   

    def testgetPairs1(self):
        _energyMatrix1 = matrix( [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]])
        p = nussinov.Nussinov('GGGAAAACCC', _energyMatrix1)
        pairs = p.getPairs();
        self.assertIsInstance(pairs, list)
        
        
    def testgetPairs2(self):
        _energyMatrix1 = matrix( [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]])
        p = nussinov.Nussinov('GGGAAAACCC', _energyMatrix1)
        pairs = p.getPairs();
        self.assertEqual(pairs,  [(0, 7), (1, 6), (2, 5), (3, 4)])
        
    def test_initialiseSmatrix(self):
        _energyMatrix1 = matrix( [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]])
        p = nussinov.Nussinov('GGGAAAACCC', _energyMatrix1)
        p._initialiseSmatrix();
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()