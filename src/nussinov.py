'''
Created on May 26, 2014

@author: jerzy
'''
import math

class NussinovError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class Nussinov(object):
    '''
    main algorithm implementation
    '''

    def __init__(self, chain, energyMatrix):
        '''
        Constructor
        '''
        self._alphabet = list('ACGU')
        self._chain = chain
        self._energyMatrix = energyMatrix  
        self._chain_length = len(chain)
        if self._chain_length > 5:
            self._initialiseSMatrix()
        else:
            raise NussinovError('Sequence too short!')

    def _getEnergy(self, xi, xj):
        if (xi and xj in self._alphabet):
            return self._energyMatrix[self._alphabet.index(xi)][self._alphabet.index(xj)]
        else:
            raise NussinovError('Asked for an energy of not existing tuple of nucleotides!')
        
    def _initialiseSMatrix(self):
        self._sMatrix = [[ 0 if j-i < 3 else float('nan')
                           for j in xrange(self._chain_length)]
                         for i in xrange(self._chain_length)]
        
    def _buildSmatrix(self):
        for d in xrange(3, self._chain_length):
            i = 0
            for j in xrange(d, self._chain_length): 
                v = []
                v.append(self._sMatrix[i+1][j-1] 
                         + self._getEnergy(self._chain[i],self._chain[j]))
                v.append(self._sMatrix[i+1][j])
                v.append(self._sMatrix[i][j-1])
                v.append(max([self._sMatrix[i][k] 
                              + self._sMatrix[k+1][j] for k in xrange(i,j)]))
                self._sMatrix[i][j] = max(v)
                i += 1
    
    def _traceback(self,i,j):
        if math.isnan(self._sMatrix[i][j]):
            raise NussinovError('sMatrix is not build yet')
            return
        if i<j:
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
        self._buildSmatrix()
        self._doTraceback()
                
    def getSMatrix(self):
        return self._sMatrix
    
    def getPairs(self):
        return self._outputPairs             
                
                
                
                
                
                