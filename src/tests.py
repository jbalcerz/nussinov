'''
Created on May 26, 2014

@author: jerzy
'''
import unittest
import nussinov


testChain1 = 'GGGAAAACCC'
testChain1 = 'GAAAAC'



testEnergyMatrix1 = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]

class NussinovTests(unittest.TestCase):
   
    def test_initialiseSMatrix1(self):
        p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
        p._initialiseSMatrix();
        printMatrix(p.getSMatrix())
        self.assertIsInstance(p.getSMatrix(), list)
        
        
    def test_getPairs1(self):
        p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
        pairs = p.getPairs();
        self.assertIsInstance(pairs, list)
        
        
    def test_getPairs2(self):
        p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
        pairs = p.getPairs();
        self.assertEqual(pairs,  [(0, 7), (1, 6), (2, 5), (3, 4)])
        

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
def printMatrix(foo):
    for table in foo:
        print "%s" %(map(str,table[0:]))