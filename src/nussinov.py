'''
Created on May 26, 2014

@author: jerzy
'''

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
        self.alphabet = list('ACGU')
        self.chain = chain
        self.energyMatrix = energyMatrix  
        self.chain_length = len(chain)
        if self.chain_length > 5:
            self._initialiseSMatrix()
        else:
            raise NussinovError('Sequence too short!')


        
    def _initialiseSMatrix(self):
        self._SMatrix = [[ 0 if j-i < 3 else float('nan')
                           for j in xrange(self.chain_length)]
                         for i in xrange(self.chain_length)]
        
    def getSMatrix(self):
        return self._SMatrix
    
    def getPairs(self):
        self._buildSmatrix()
        return [(0,0)]
    
    def _getEnergy(self, xi, xj):
        if (xi and xj in self.alphabet):
            return self.energyMatrix[self.alphabet.index(xi)][self.alphabet.index(xj)]
        else:
            raise NussinovError('Asked for an energy of not existing tuple of nucleotides!')
        
    def _buildSmatrix(self):
        for d in xrange(3, self.chain_length):
            i = 0
            for j in xrange(d, self.chain_length): 
                v = []
                v.append(self._SMatrix[i+1][j-1] 
                         + self._getEnergy(self.chain[i],self.chain[j]))
                v.append(self._SMatrix[i+1][j])
                v.append(self._SMatrix[i][j-1])
                v.append(max([self._SMatrix[i][k] 
                              + self._SMatrix[k+1][j] for k in xrange(i,j)]))
                self._SMatrix[i][j] = max(v)
                i += 1
                
                
                
                
                
                
                
                
                