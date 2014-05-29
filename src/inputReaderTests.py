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
        with self.assertRaises(inputReader.InputReaderError) as cm:
            inputReader.InputReader('')
        the_exception = cm.exception
        self.assertEqual(the_exception.value,1)
        
    def test_InputReader_filesNoArguments(self):    
        
        with self.assertRaises(SystemExit):
            with self.assertRaises(getopt.GetoptError):
                inputReader.InputReader(['-i'])
        
        with self.assertRaises(SystemExit):
            with self.assertRaises(getopt.GetoptError):
                inputReader.InputReader(['-o'])
        
#     def test_InputReader_inputFile2(self):    
#         
#         p = inputReader.InputReader(['-i', 'exampleInput.txt'])
#         with self.assertRaises(inputReader.InputReaderError) as cm:
#             p = inputReader.InputReader('')
#         the_exception = cm.exception
#         self.assertEqual(the_exception.value,1)
        
        

#     def test_InputReader_help(self):    
#         
#         p = inputReader.InputReader(['-h'])
#          
         
        
# class InputReaderTest(unittest.TestCase): 
#         
#    
#         

            
#     def test_InputReader_NoInputDefaultFilesExist(self):
#         p = inputReader.InputReader("")
# # tutaj usunac a potem stworzyc plik i wpuscic tam dane
#         self.assertEqual(p.inputfile == 'input.txt')
#         self.assertEqual(p.outputfile == 'output.txt')
#         self.assertEqual(p.inputfile == 'input.txt')
#             
#             
#     def test_InputReaderFileNamesGiven(self):   
#         p = inputReader.InputReader("-i in1.txt -o out1.txt")
#         self.assertEqual(p.inputfile == 'in1.txt')
#         self.assertEqual(p.outputfile == 'out1.txt"')  
#         
#     def test_InputReaderFileNamesGiven(self):
#         p = inputReader.InputReader("-i in1.txt -o out1.txt")
#         self.assertEqual(p.inputfile == 'in1.txt')
#         self.assertEqual(p.outputfile == 'out1.txt"')  
#         
        
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

