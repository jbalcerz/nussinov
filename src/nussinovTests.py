'''
Created on May 26, 2014

@author: jerzy
'''
import nussinov, inputReader
import unittest, os

testChain0 = 'GAAAAC'
testChain1 = 'GGGAAAACCC'


alphabet = list('ACGU')
testEnergyMatrix1 = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
testSMatrixForChain1 = [[0, 0, 0, 0, 0, 0, 0, 3, 6, 9], [0, 0, 0, 0, 0, 0, 0, 3, 6, 6], [0, 0, 0, 0, 0, 0, 0, 3, 3, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
testOutputPairs = [(0, 9), (1, 8), (2, 7)]

class NussinovTests(unittest.TestCase):
   
    def test_initialiseSMatrix1(self):
        p = nussinov.Nussinov(testChain0, testEnergyMatrix1)
        p._initialiseSMatrix();
        self.assertIsInstance(p.getSMatrix(), list)
        
    def test_getEnergy1(self):
        p = nussinov.Nussinov(testChain0, testEnergyMatrix1)
        with self.assertRaises(nussinov.NussinovError) as cm:
            p._getEnergy('A', 'X')
        the_exception = cm.exception
        self.assertEqual(the_exception.value, 1)
        print the_exception
               
               
    def test_getEnergy2(self):
        p = nussinov.Nussinov(testChain0, testEnergyMatrix1)
        self.assertEqual(p._getEnergy('A','C'),0)
        self.assertEqual(p._getEnergy('U','U'),0)
        self.assertEqual(p._getEnergy('G','C'),3)
      
    def test_buildSMatrix1(self):
        p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
        p._buildSmatrix()
        self.assertEqual(p.getSMatrix(), testSMatrixForChain1)
#         printMatrix(p.getSMatrix())
        
    def test_doTraceback1(self):
        p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
        with self.assertRaises(nussinov.NussinovError) as cm:
            p._doTraceback()
        the_exception = cm.exception
        self.assertEqual(the_exception.value,2)
        print the_exception
        
        
    def test_doTraceback2(self):
        p = nussinov.Nussinov(testChain1, testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), testOutputPairs)



class NussinovWeirdChainsTest(unittest.TestCase):

    def test_doTraceback3(self):
        p = nussinov.Nussinov('CAAGGAAC', testEnergyMatrix1)
        p._minLoop = 3
        p.calculate()
        self.assertEqual(p.getPairs(), [(0, 3), (4, 7)])
        
    def test_doTraceback4(self):
        p = nussinov.Nussinov('AUAUAUAUA', testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(1, 8), (2, 7), (3, 6)])
        
    def test_doTraceback5(self):
        p = nussinov.Nussinov('AUAUAUAUA', testEnergyMatrix1)
        p.calculate()
        self.assertEqual(p.getPairs(), [(1, 8), (2, 7), (3, 6)])
    def test_doTraceback6(self):
        p = nussinov.Nussinov('AUAUAUAUA', testEnergyMatrix1)
        p._minLoop = 2
        p.calculate()
        self.assertEqual(p.getPairs(), [(1, 8), (2, 7), (3, 6), (4, 5)])
    def test_doTraceback7(self):
        p = nussinov.Nussinov('AUAUACUAUA', testEnergyMatrix1)
        p._minLoop = 2
        p.calculate()
        self.assertEqual(p.getPairs(), [(1, 9), (2, 8), (3, 7), (4, 6)])    

    
def printMatrix(foo):
    for table in foo:
        print "%s" %(map(str,table[0:]))