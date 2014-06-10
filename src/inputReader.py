'''
    Created on May 26, 2014
    
    @author: jerzy
    '''

import sys, getopt, ast
import numpy
from itertools import combinations


class InputReader(object):
    '''
        
        '''
    #@profile
    def __init__(self,argv):
        '''
            Constructor
            '''
        self._helpText = 'main.py -i <inputfile> -o <outputfile> -r <raw data> ' \
                          '-m <min. elemenths in loop> -e <energy matrix> \n' \
                          'default: [-i input.txt -o output.txt -m 4 '\
                          r'-e [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]] ]'
        
        self._dafaultInputFile = 'input.txt'
        self._dafaultOutputFile = 'output.txt'
        self._EnergyMatrix = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
        self._MinLoop = 4
        self._minimumChainLength = 2
        self._alphabet = list('ACGU')

        if ('-h' in argv):
                self._printHelpAndExit()
                
        if not ('-i' in argv):
            self._handleNoInputGiven()
            
        if not ('-o' in argv):
            self._handleNoOutputGiven()
            
        if (0 != len(argv)):
            try:
                opts, args = getopt.getopt(argv,"hi:o:r:m:e:",["ifile=","ofile=","rdata="])
            except getopt.GetoptError:
                self._printHelpAndExit()
            
            self._checkIfOptsOk(opts)
            
            for opt, arg in opts:
                if opt in ("-i", "--ifile"):
                    self._handleInputFileGiven(arg)
                elif opt in ("-o", "--ofile"):
                    self._handleOutputFileGiven(arg)
                elif opt in ("-r", "--rdata"):
                    self._handleRawDataGiven(arg)
                elif opt == "-m":#trzeba zrobic handler
                    self._handleMinLoop(arg)
                elif opt == "-e":
                    self._handleEnergyMatrix(arg)

    def _handleMinLoop(self, arg):
        try:
            self._MinLoop = int(arg)
        except ValueError:
            raise InputReaderException(7,self, 'wrong value of minimal loop length')
        if self._MinLoop  < 0:
            raise InputReaderException(7,self, 'too small value of minimal loop length')
              
    
    def _handleEnergyMatrix(self, arg):
        try:
            tmp = ast.literal_eval(arg)
            if (numpy.array(tmp).shape == (4,4)):
                self._EnergyMatrix = tmp
                print tmp
            else:
                raise InputReaderException(7,self, 'wrong size of an energy matrix')
        except:
            raise InputReaderException(7,self, 'problem with parsing energy matrix')
                    
    def _handleNoInputGiven(self):
        try:
            self._inputFileObj = open(self._dafaultInputFile)
        except IOError as e:
            if e.errno == 2:
                self._handleFileError("can not open default input: input.txt")
    
    def _handleNoOutputGiven(self):
        try:
            self._outputFileObj = open(self._dafaultOutputFile, "w+")
        except IOError as e:
            if e.errno == 2:
                self._handleFileError("can not open default output file!")
    
    def _checkIfOptsOk(self,opts):
        if ([] == opts):
                raise InputReaderException(6, self, 'incorrect parameters')
        options = [i[0] for i in opts]
        options_pairs = [i for i in combinations(options,2)]
        conflicting_opts = [('-i', '-r'), ('-r', '-i'), ('-i', '--rdata'), ('--rdata', '-i'),
             ('--ifile', '-r'), ('-r', '--ifile'), ('--ifile', '--rdata'),
             ('--rdata', '--ifile')]
        
        if (set(options_pairs) & set(conflicting_opts)):
            raise InputReaderException(5,self, "-i and -r options can not be used together")
            sys.exit(2)
    
    def _handleInputFileGiven(self, arg):
        try:
            self._inputFileObj = open(arg)
        except IOError as e:
            if e.errno == 2:
                self._handleFileError("can not open given input file!")
    
    def _handleOutputFileGiven(self,arg):
        try:
            self._outputFileObj = open(arg, "w+")
        except IOError as e:
            if e.errno == 2:
                self._handleFileError("can not open given output file!")
    
    def _handleRawDataGiven(self,arg):
        try:
            self._inputFileObj = open("lastRawInput.txt", "w+")
            self._inputFileObj.write(arg + "\n")
            self._inputFileObj.close()
            self._inputFileObj = open("lastRawInput.txt")
        except IOError as e:
            if e.errno == 2:
                self._handleFileError("can not create lastRawInput.txt file")

    def _printHelpAndExit(self):
        print self._helpText
        self.closeFiles()
        sys.exit(0)
    
    def _handleFileError(self, message):
        self.closeFiles()
        raise InputReaderException(1,self, message)
        sys.exit(2)
    
    def _check_line(self, line):
        if(len(line) < self._minimumChainLength):
            raise InputReaderException(2,self,'input string to short!')
        
        
        for i,x in enumerate(line):
            if x not in self._alphabet :
                raise InputReaderException(3,self, 'wrong symbol %s at position %d' % (x, i))
    
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
    
    def get_EnergyMatrix(self):
        return self._EnergyMatrix
    
    def get_MinLoop(self):
        return self._MinLoop
        
    def get_outputFileObject(self):
        try:
            self._outputFileObj
        except NameError:
            raise InputReaderException(4, self, 'output file object was not created')
        else:
            return self._outputFileObj
        
    def closeFiles(self):
        try:
            self._outputFileObj
        except (NameError, AttributeError):
            pass
        else:
            self._outputFileObj.close()
        
        try:
            self._inputFileObj
        except (NameError, AttributeError):
            pass
        else:
            self._inputFileObj.close()

class InputReaderException(Exception):
    def __init__(self, value, inputReaderObject, message):
        self.value = value
        self.message = message
        inputReaderObject.closeFiles()
        
        
        
    def __str__(self):
        return ("\nERROR (" + str(self.value) + "): " +  self.message)
