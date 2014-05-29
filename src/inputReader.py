'''
Created on May 26, 2014

@author: jerzy
'''

import sys, getopt, os

from itertools import permutations, combinations, product
from operator import eq, __eq__


class InputReader(object):
    '''
        Let's make a nice class to encapsulate some methods with "_" sign.
        
        The input should be handeled here. What should it do:
        - display prompt to the user 
        - read data from keyboard (one line)...
        - or ask use for a path and read data form file
        - check if data is correct (letters in sequence ok?)
        - to the main procedute I want to receive a string containing symbols 
        form group {ACGU} 
        - as we assume that loops should have at least 4 nucleotides, 
        then test chain should have at least 6 nucleotides - am I right??????
        - remember to add exceptions catching - in case of problems with files!!
           
        what to add later:
        - should we read energy matrix form user?
        - should we read the smallest noumber of elements in a loop? 
          (compare pages 43 and 48 in Nowak's lecture notes)
        - in case of reading from file: maybe read each line of file as separate 
          chain and make it possible to iterate through them?
        - read data form RNA STRAND database - it is actual database that you 
          can download (around 30MB) form http://www.rnasoft.ca/strand/ 
          using this would be really nice! 
          (watch out - there is a special formatting and more than 4 symbols in chains)
        
        
        
        1. co jesli sie nic nie wpisze? 
            - 
    '''
    def __init__(self,argv):
        '''
        Constructor
        '''
        self._dafaultInputFile = 'input.txt'
        self._dafaultOutputFile = 'output.txt'
        self._minimumChainLength = 2
        self._alphabet = list('ACGU')
        try:
            opts, args = getopt.getopt(argv,"hi:o:r:",["ifile=","ofile=","rdata="])
        except getopt.GetoptError:
            self._printHelp()
            sys.exit()
            
        self._checkIfOptsOk(opts)
        
        if opts == []:
            self._handleNoOptions()
         
        for opt, arg in opts:
            if opt == '-h':
                self._printHelp()
            elif opt in ("-i", "--ifile"):
                self._handleInputFileGiven(arg)
            elif opt in ("-o", "--ofile"):
                self._handleOutputFileGiven(arg) 
            elif opt in ("-r", "--rdata"):
                self._handleRawDataGiven(arg)

    def _checkIfOptsOk(self,opts):
        x = []
        for l in list(product(['-i', '--ifile'],['-r', '--rdata'])): 
            x= x + list(permutations(l))
        if opts[0] in x:
            raise InputReaderError(5,"-i and -r options can not be used together")
            sys.exit(2)
        

    def _handleInputFileGiven(self, arg):
        try:
            self._inputFileObj = open(arg)
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("can not open given input file!")
    
    def _handleOutputFileGiven(self,arg):
        try:
            self._outputFileObj = open(arg, "w+")
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("can not open given output file!")
                
    def _handleRawDataGiven(self,arg):
        try:
            self._inputFileObj = open("input.txt", "w+")
            self._inputFileObj.write(arg)
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("can not create input.txt file")
    
    def _handleNoOptions(self):
        try:
            self._inputFileObj = open(self._dafaultInputFile)
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("no input file, default: input.txt")
        try:
            self._outputFileObj = open(self._dafaultOutputFile, "w+")
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("can not open/create output.txt")



    def _printHelp(self):
        print 'test.py -i <inputfile> -o <outputfile>'
        
    def _handleNoInputFile(self, message):
        raise InputReaderError(1,message)
        sys.exit(2)
        
    def _check_line(self, line):
        if(len(line) < self._minimumChainLength):
            raise InputReaderError(2,'input string to short!')
        
        for i,x in enumerate(line):
            if x not in self._alphabet :
                raise InputReaderError(3, 'wrong symbol %s at position %d' % (x, i))
        
    def __iter__(self):
        return self        
    
    def next(self):
        return self.get_one_line()
    
    def get_one_line(self):
        try:
            line = self._inputFileObj.next()
            if line[-1] == '\n':
                line = line[0:-1]
        except StopIteration:
            self._inputFileObj.close()
            raise
        self._check_line(line)
        return line
    
    def get_outputFileObject(self):
        try:
            self._outputFileObj
        except NameError:
            raise InputReaderError(4, 'output file object was not created')
        else:
            return self._outputFileObj
        
        
class InputReaderError(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
        print self.__str__()
    def __str__(self):
        return ("\nExcepiton: in " +  os.path.basename(__file__) + " module: \n\tcode: " 
          + repr(self.value) + "\n\tmessage: " + self.message)
              
        
        
        
        
        
        
        
        
    
        