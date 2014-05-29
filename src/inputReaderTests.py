'''
Created on May 29, 2014

@author: jerzy
'''

import inputReader
import unittest, os, getopt
    
class InputReaderTest(unittest.TestCase):
    
     
    def test_InputReader_NoOpt(self):    
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except OSError:
            pass
         
        with self.assertRaises(inputReader.InputReaderError) as cm:
            inputReader.InputReader('')
        the_exception = cm.exception
        self.assertEqual(the_exception.value,1)
          
    def test_InputReader_Default1(self):    
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except OSError:
            pass
         
        testChain = 'GGGAAAACCC'
        myInFile = open("input.txt", "w+")
        myInFile.write(testChain)
        myInFile.close()
        p = inputReader.InputReader('')
        self.assertEqual(p.next(), testChain)
         
    def test_InputReader_Default2(self):    
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except OSError:
            pass
          
        myInFile = open("input.txt", "w+")
        myInFile.write("GGGAAAACCC\nAUAUACUAUA\nACGCACGC")
        myInFile.close()
         
        p = inputReader.InputReader('')
        self.assertEqual(p.next(), 'GGGAAAACCC')
        self.assertEqual(p.next(), 'AUAUACUAUA')
        self.assertEqual(p.next(), 'ACGCACGC')
          
    def test_InputReader_help(self):    
        inputReader.InputReader(['-h'])
         
    def test_InputReader_filesNoArguments(self):   
          
        with self.assertRaises(SystemExit):
            with self.assertRaises(getopt.GetoptError):
                inputReader.InputReader(['-i'])
         
        with self.assertRaises(SystemExit):
            with self.assertRaises(getopt.GetoptError):
                inputReader.InputReader(['-o'])
                 
    def test_InputReader_ReadSpecyficFile(self):
         
        with self.assertRaises(inputReader.InputReaderError) as cm:
            inputReader.InputReader(['-i', 'exampleInput2.txt'])
        the_exception = cm.exception
        self.assertEqual(the_exception.value,1)
         
    def test_InputReader_ReadSpecyficFile2(self):
              
        try:
            os.remove("input1.txt")
        except OSError:
            pass
         
        myInFile = open("input1.txt", "w+")
        myInFile.write("GGGAAAACCC\nAUAUACUAUA\nACGCACGC")
        myInFile.close()
         
        p = inputReader.InputReader(['-i', 'input1.txt'])
        self.assertEqual(p.next(), 'GGGAAAACCC')
        self.assertEqual(p.next(), 'AUAUACUAUA')
        self.assertEqual(p.next(), 'ACGCACGC')
         
        os.remove("input1.txt")
         
    def test_InputReader_OutputSpecyficFile(self):
         
        inputReader.InputReader(['-o', 'output.txt'])
        self.assertIsInstance(open("output.txt"), file)
         
         
    def test_InputReader_RawInput(self):
        
        
        with self.assertRaises(inputReader.InputReaderError) as cm:
            inputReader.InputReader(['-i', '-r'])
        with self.assertRaises(inputReader.InputReaderError) as cm:
            inputReader.InputReader(["-r", "-i"])

        p = inputReader.InputReader(['-r', 'GGGAAAACCC'])
        self.assertEqual(p.next(), 'GGGAAAACCC')
        
        
    
    #kombindacje -i i -o
    
    #-r i -o
    
    
    #-i i -r
    
    #-i -o -r
    
    #swoj alphabet??
        
       
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

