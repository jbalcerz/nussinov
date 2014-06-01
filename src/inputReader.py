'''
    Created on May 26, 2014
    
    @author: jerzy
    '''

import sys, getopt, os


from itertools import permutations,  product


class InputReader(object):

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
        
        try:
            if not ('-o' in opts[0]):
                self._handleNoOutputGiven()
        except IndexError:
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
        except IOError:
            print>>sys.stderr,'Error: Can\'t open default output file.'
            sys.exit(2);


    def _checkIfOptsOk(self,opts):
        x = []
        for l in list(product(['-i', '--ifile'],['-r', '--rdata'])):
            x = x + list(permutations(l))
        if opts[0] in x:
            print>>sys.stderr,'Error: -i and -r options can not be used together'
            sys.exit(2);
    
    
    def _handleInputFileGiven(self, arg):
        try:
            self._inputFileObj = open(arg)
        except AttributeError, IOError:
            print>>sys.stderr,'Error: Can\'t open given input file.'
            sys.exit(2);


    def _handleOutputFileGiven(self,arg):
        try:
            self._outputFileObj = open(arg, "w+")
        except IOError:
            print>>sys.stderr,'Error: Can\'t open given output file.'
            sys.exit(2);

    def _handleRawDataGiven(self,arg):
        try:
            self._inputFileObj = open("input.txt", "w+")
            self._inputFileObj.write(arg + "\n")
            self._inputFileObj.close()
            self._inputFileObj = open("input.txt")
        except IOError:
            print>>sys.stderr,'Error: Can\'t create input file \"input.txt\".'
            sys.exit(2);


    def _handleNoOptionsGiven(self):
        try:
            self._inputFileObj = open(self._dafaultInputFile)
        except IOError:
            print>>sys.stderr,'Error: No input file, using default file \"input.txt\" instead.'
            sys.exit(2);
        try:
            self._outputFileObj = open(self._dafaultOutputFile, "w+")
        except IOError:
            print>>sys.stderr,'Error: Can\'t open/create output file \"output.txt\".'
            sys.exit(2);
    

    def _printHelp(self):
        print(self._helpText)
        sys.exit(2)


    def _check_line(self, line):
        if(len(line) < self._minimumChainLength):
            print>>sys.stderr,'Error: Input string is too short!'
            sys.exit(2);
        
        for i,x in enumerate(line):
            if x not in self._alphabet :
                print>>sys.stderr,'Error: Wrong symbol \'%s\' at position %d' % (x,i)
                sys.exit(3);
    
    
    def __iter__(self):
        return self
    
    
    def next(self):
        return self.get_one_line()


    def get_inputFileObject(self):
        try:
            self._inputFileObj
        except NameError:
            print>>sys.stderr,'Error: Input file object wasn\'t created'
            sys.exit(4);
        else:
            return self._inputFileObj
            
            
    def get_outputFileObject(self):
        try:
            self._outputFileObj
        except NameError:
            print>>sys.stderr,'Error: Output file object wasn\'t created'
            sys.exit(4);
        else:
            return self._outputFileObj


    def get_one_line(self):
        try:
            line = get_inputFileObject.next()
            if line[-1] == '\n':
                line = line[0:-1]
        except StopIteration:
            self._inputFileObj.close()
            raise
        self._check_line(line)
        return line


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
