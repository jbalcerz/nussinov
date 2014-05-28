'''
Created on May 26, 2014

@author: jerzy
'''
import unittest
from nussinov import *

testChain0 = 'GAAAAC'
testChain1 = 'GGGAAAACCC'

alphabet = list('ACGU')
testEnergyMatrix1 = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
testSMatrixForChain1 = [[0, 0, 0, 0, 0, 0, 0, 3, 6, 9], [0, 0, 0, 0, 0, 0, 0, 3, 6, 6], [0, 0, 0, 0, 0, 0, 0, 3, 3, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

class NussinovTests(unittest.TestCase):
   
    def test_initialiseSMatrix1(self):
        p = Nussinov(testChain0, testEnergyMatrix1)
        p._initialiseSMatrix();
#         printMatrix(p.getSMatrix())
        self.assertIsInstance(p.getSMatrix(), list)
    def test_getEnergy1(self):
        p = Nussinov(testChain0, testEnergyMatrix1)
        try:
            self.assertRaises(NussinovError, p._getEnergy('A', 'X'))
        except NussinovError as e:
            print 'exception occurred:\n', e.value, '\n'
         
    def test_getEnergy2(self):
        p = Nussinov(testChain0, testEnergyMatrix1)
        self.assertEqual(p._getEnergy('A','C'),0)
        self.assertEqual(p._getEnergy('U','U'),0)
        self.assertEqual(p._getEnergy('G','C'),3)
      
    def test_buildSMatrix1(self):
        p = Nussinov(testChain1, testEnergyMatrix1)
        p._buildSmatrix()
        self.assertEqual(p.getSMatrix(), testSMatrixForChain1)
        printMatrix(p.getSMatrix())
        
         
#     def test_getPairs1(self):
#         p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
#         pairs = p.getPairs();
#         self.assertIsInstance(pairs, list)
#          
#          
#     def test_getPairs2(self):
#         p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
#         pairs = p.getPairs();
#         self.assertEqual(pairs,  [(0, 7), (1, 6), (2, 5), (3, 4)])
#          

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
def printMatrix(foo):
    for table in foo:
        print "%s" %(map(str,table[0:]))