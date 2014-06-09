'''
Created on May 29, 2014

@author: jerzy
'''

import inputReader, main
import unittest, os, getopt
    
class InputReaderTest(unittest.TestCase):
    
     
    def test_InputReader_NoOpt(self):    
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except OSError:
            pass
        with self.assertRaises(inputReader.InputReaderException) as cm:
            inputReader.InputReader('')
        self.assertEqual((cm.exception).value,1)
#         self.assertEqual(main.main(''),1)
        
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
#           
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
            

    def test_InputReader_askForHelp(self):   
        with self.assertRaises(SystemExit):
            inputReader.InputReader(['-h'])
        
        with self.assertRaises(SystemExit):
            inputReader.InputReader(['-h','-i','-o'])
     
    def test_InputReader_filesNoArguments(self):   
           
        try:
            os.remove("input.txt")
            os.remove("output.txt")
        except OSError:
            pass
             
        myInFile = open("input.txt", "w+")
        myInFile.write("GGGAAAACCC\nAUAUACUAUA\nACGCACGC")
        myInFile.close()
        
        with self.assertRaises(SystemExit):
            with self.assertRaises(getopt.GetoptError):
                inputReader.InputReader(['-i'])
          
        with self.assertRaises(SystemExit):
            with self.assertRaises(getopt.GetoptError):
                inputReader.InputReader(['-o'])
                  
    def test_InputReader_ReadSpecyficFile(self):
          
        with self.assertRaises(inputReader.InputReaderException) as cm:
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
        
        try:
            os.remove("input.txt")
            os.remove("output1.txt")
        except OSError:
            pass
             
        myInFile = open("input.txt", "w+")
        myInFile.write("GGGAAAACCC\nAUAUACUAUA\nACGCACGC")
        myInFile.close()
        
        
        inputReader.InputReader(['-o', 'output1.txt'])
        self.assertIsInstance(open("output1.txt"), file)
          
          
    def test_InputReader_RawInput(self):
         

        p = inputReader.InputReader(['-r', 'GGGAAAACCC'])
        self.assertEqual(p.next(), 'GGGAAAACCC')
         
    
    def test_InputReader_ParametersCombinations(self):
        
        try:
            os.remove("input.txt")
            os.remove("output1.txt")
        except OSError:
            pass
             
        myInFile = open("input.txt", "w+")
        myInFile.write("GGGAAAACCC\nAUAUACUAUA\nACGCACGC")
        myInFile.close()
        
        
        inputReader.InputReader(['-i', 'exampleInput.txt', '-o', 'output22.txt'])
        self.assertIsInstance(open("output22.txt"), file)
        
                 
        with self.assertRaises(inputReader.InputReaderException):
            inputReader.InputReader(['-i', '-r'])
        with self.assertRaises(inputReader.InputReaderException):
            inputReader.InputReader(['-r', 'kicha', '-i', 'kicha','-o','kicha'])
             
    def test_InputReader_ParametersCombinations2(self):
        
        try:
            os.remove("input.txt")
            os.remove("output1.txt")
        except OSError:
            pass
             
        myInFile = open("input.txt", "w+")
        myInFile.write("GGGAAAACCC\nAUAUACUAUA\nACGCACGC")
        myInFile.close()
        
        

        
        p = inputReader.InputReader(['-m', '5', '-e', '[[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]', '-i', 'exampleInput.txt', '-o', 'output22.txt'])         
        self.assertEqual(p.get_MinLoop(), 5)
        self.assertEqual(p.get_EnergyMatrix(), [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]])
         
        with self.assertRaises(inputReader.InputReaderException):
            p = inputReader.InputReader(['-m', 'p', '-e', '[[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]', '-i', 'exampleInput.txt', '-o', 'output22.txt'])         
#         
        with self.assertRaises(inputReader.InputReaderException):
            p = inputReader.InputReader(['-m', '5', '-e', '[[0,0,0],[0,0,3,0],[0,3,0,3],[2,0,1,0]]', '-i', 'exampleInput.txt', '-o', 'output22.txt'])         
        
        self.assertIsInstance(open("output22.txt"), file)     
        
       
        #         with self.assertRaises(inputReader.InputReaderException):
if __name__ == "__main__":
    unittest.main()

