'''
Created on May 26, 2014

@author: jerzy
'''
from src import nussinov as nus
import unittest

testChain0 = 'GAAAAC'
testChain1 = 'GGGAAAACCC'

defaultMinLoop = 4

alphabet = list('ACGU')
testEnergyMatrix1 = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
testSMatrixForChain1 = [[0, 0, 0, 0, 0, 0, 0, 3, 6, 9], [0, 0, 0, 0, 0, 0, 0, 3, 6, 6], [0, 0, 0, 0, 0, 0, 0, 3, 3, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
testOutputPairs = [(0, 9), (1, 8), (2, 7)]

class NussinovTests(unittest.TestCase):
#    
#     def test_initialiseSMatrix1(self):
#         p = nus.Nussinov(testChain0, defaultMinLoop, testEnergyMatrix1)
#         p._initialiseSMatrix();
#         self.assertIsInstance(p.getSMatrix(), list)
#          
    def test_getEnergy1(self):
        p = nus.Nussinov(testChain0, defaultMinLoop, testEnergyMatrix1)
        with self.assertRaises(nus.NussinovException) as cm:
            p._getEnergy('A', 'X')
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 1)
        print the_exception
                
                
    def test_getEnergy2(self): 
        p = nus.Nussinov(testChain0, defaultMinLoop, testEnergyMatrix1)
        self.assertEqual(p._getEnergy('A','C'),0)
        self.assertEqual(p._getEnergy('U','U'),0)
        self.assertEqual(p._getEnergy('G','C'),3)
       
    def test_buildSMatrix1(self):
        p = nus.Nussinov(testChain1, defaultMinLoop, testEnergyMatrix1)
        p._buildSmatrix()
        self.assertEqual(p.getSMatrix(), testSMatrixForChain1)
#         printMatrix(p.getSMatrix())
         
    def test_doTraceback1(self):
        p = nus.Nussinov(testChain1, defaultMinLoop, testEnergyMatrix1)
        with self.assertRaises(nus.NussinovException) as cm:
            p._doTraceback()
        the_exception = cm.exception
        self.assertEqual(the_exception.value,2)
        print the_exception
         
         
    def test_doTraceback2(self):
        p = nus.Nussinov(testChain1, defaultMinLoop, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), testOutputPairs)
 
 
 
class NussinovMinLoopTests(unittest.TestCase):
 
    def test_calculateLoop6(self):
        p = nus.Nussinov('AUAUAUAU', 6, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7)])
     
    def test_calculateLoop5(self):
        p = nus.Nussinov('AUAUAUAU', 5, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7)])
     
    def test_calculateLoop4(self):
        p = nus.Nussinov('AUAUAUAU', 4, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7), (1, 6)])
#     
    def test_calculateLoop3(self):
        p = nus.Nussinov('AUAUAUAU', 3, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7), (1, 6)])
         
    def test_calculateLoop2(self):
        p = nus.Nussinov('AUAUAUAU', 2, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7), (1, 6), (2, 5)])
         
    def test_calculateLoop1(self):
        p = nus.Nussinov('AUAUAUAU', 1, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7), (1, 6), (2, 5)])

    def test_calculateLoop0(self):
        p = nus.Nussinov('AUAUAUAU', 0, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 7), (1, 6), (2, 5), (3, 4)])


def printMatrix(foo):
    for table in foo:
        print "%s" %(map(str,table[0:]))
        
        
        
        
       
if __name__ == "__main__":
    unittest.main()