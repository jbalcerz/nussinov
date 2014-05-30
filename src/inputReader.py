'''
Created on May 26, 2014

@author: jerzy
'''

import sys, getopt, os


from itertools import permutations,  product


class InputReader(object):
    '''

    '''
    def __init__(self,argv):
        '''
        Constructor
        '''
        self._helpText = 'main.py -i <inputfile> -o <outputfile> -r <raw data> \n' \
                          '\t[-i input.txt -o output.txt]'
        
        
        self._dafaultInputFile = 'input.txt'
        self._dafaultOutputFile = 'output.txt'
        self._minimumChainLength = 2
        self._alphabet = list('ACGU')
        try:
            opts, args = getopt.getopt(argv,"hi:o:r:",["ifile=","ofile=","rdata="])
        except getopt.GetoptError:
            self._printHelp()
            sys.exit()
        
        if not ('-o' in opts[0]):
            self._handleNoOutputGiven()

        if opts == []:
            self._handleNoOptionsGiven()
            return
        
        self._checkIfOptsOk(opts)
        
        for opt, arg in opts:
            if opt == '-h':
                self._printHelp()
            elif opt in ("-i", "--ifile"):
                self._handleInputFileGiven(arg)
            elif opt in ("-o", "--ofile"):
                self._handleOutputFileGiven(arg) 
            elif opt in ("-r", "--rdata"):
                self._handleRawDataGiven(arg)

    def _handleNoOutputGiven(self):
        try:
            self._outputFileObj = open(self._dafaultOutputFile, "w+")
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("can not open default output file!")   
                 
    def _checkIfOptsOk(self,opts):
        x = []
        for l in list(product(['-i', '--ifile'],['-r', '--rdata'])): 
            x = x + list(permutations(l))
        if opts[0] in x:
            raise InputReaderException(5,"-i and -r options can not be used together")
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
            self._inputFileObj.write(arg + "\n")
            self._inputFileObj.close()
            self._inputFileObj = open("input.txt")
        except IOError as e:
            if e.errno == 2:
                self._handleNoInputFile("can not create input.txt file")
    
    def _handleNoOptionsGiven(self):
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
        print self._helpText
        sys.exit(2)
        
    def _handleNoInputFile(self, message):
        raise InputReaderException(1,message)
        sys.exit(2)
        
    def _check_line(self, line):
        if(len(line) < self._minimumChainLength):
            raise InputReaderException(2,'input string to short!')
           
        
        for i,x in enumerate(line):
            if x not in self._alphabet :
                raise InputReaderException(3, 'wrong symbol %s at position %d' % (x, i))
               
        
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
            raise InputReaderException(4, 'output file object was not created')
        else:
            return self._outputFileObj
    def closeFiles(self):
        
        try:
            self._outputFileObj
        except NameError:
            pass
        else:
            self._outputFileObj.close()
        
        try:
            self._inputFileObj
        except NameError:
            pass
        else:
            self._inputFileObj.close()
        
class InputReaderException(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
 
        
        
    def __str__(self):
        return ("\nERROR (" + str(self.value) + "): " +  self.message)
              
        
        
        
        
        
        
        
        
    
        