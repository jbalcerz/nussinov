'''
Created on May 26, 2014

@author: jerzy
'''
import math, os

class Nussinov(object):
    '''
    main algorithm implementation
    '''

    def __init__(self, chain, minLoop, energyMatrix):
        '''
        Constructor
        '''
        self._alphabet = list('ACGU')
        self._chain = chain
        self._energyMatrix = energyMatrix  
        self._chain_length = len(chain)
        self._minLoop = minLoop
        self._initialiseSMatrix()

    def _initialiseSMatrix(self):
        self._sMatrix = [[ 0 if j - i <= self._minLoop else float('nan')
                           for j in xrange(self._chain_length)]
                         for i in xrange(self._chain_length)]

    def _getEnergy(self, xi, xj):
        if (xi and xj in self._alphabet):
            return self._energyMatrix[self._alphabet.index(xi)][self._alphabet.index(xj)]
        else:
            raise NussinovException(1,'Asked for an energy of not existing tuple of nucleotides!')

                
    def _buildSmatrix(self):
        for d in xrange(1, self._chain_length):
            i = 0
            for j in xrange(d, self._chain_length): 
                if (j-i<=self._minLoop):
                    self._sMatrix[i][j] = 0
                else:
                    v = []
                    v.append(self._sMatrix[i+1][j-1] 
                             + self._getEnergy(self._chain[i],self._chain[j]))
                    v.append(self._sMatrix[i+1][j])
                    v.append(self._sMatrix[i][j-1])
                    v.append(max([self._sMatrix[i][k] 
                                  + self._sMatrix[k+1][j] for k in xrange(i,j)]))
                    self._sMatrix[i][j] = max(v)
                i += 1
                
                
                #@profile
    def _traceback(self,i,j):
        if math.isnan(self._sMatrix[i][j]):
            raise NussinovException(2,'sMatrix is not build yet!')
            return
        if i < j:
            if self._sMatrix[i][j] == self._sMatrix[i+1][j]:
                self._traceback(i+1,j)
            elif self._sMatrix[i][j] == self._sMatrix[i][j-1]:
                self._traceback(i,j-1)
            elif self._sMatrix[i][j] == (self._sMatrix[i+1][j-1] 
                                         + self._getEnergy(self._chain[i],self._chain[j])):
                self._outputPairs.append((i,j))
                self._traceback(i+1,j-1)
            else:
                for k in range(i+1,j):
                    if self._sMatrix[i][j] == (self._sMatrix[i][k] 
                                               + self._sMatrix[k+1][j]):
                        self._traceback(i,k)
                        self._traceback(k+1,j)
                        break
                    
            
    def _doTraceback(self):
        self._outputPairs = []
        self._traceback(0,self._chain_length - 1)           

    def calculate(self):
        if self._chain_length < self._minLoop + 2:
            self._outputPairs = [()]
            return 
        self._buildSmatrix()
        self._doTraceback()
                
    def getSMatrix(self):
        return self._sMatrix
    
    def getPairs(self):
        return self._outputPairs             
                
                
                

class NussinovException(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
    def __str__(self):
        return ("\nExcepiton: in " +  os.path.basename(__file__) + " module: \n\tcode: " 
                + repr(self.value) + "\n\tmessage: " + self.message)
        
    
    
                
                