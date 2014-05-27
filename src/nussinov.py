'''
Created on May 26, 2014

@author: jerzy
'''

class Nussinov(object):
    '''
    main algorithm implementation
    '''


    def __init__(self, chain, energyMatrix):
        '''
        Constructor
        '''
        self.chain = chain
        self.energyMatrix = energyMatrix  
        self.chain_length = len(chain)
        if self.chain_length > 5:
            self._initialiseSmatrix()
        else:
            print("to short sentence!") #TODO: throw exeption!
        
        
    def _initialiseSMatrix(self):
        self._SMatrix = [[ 0 if j-i < 3 else float('nan') for j in xrange(self.chain_length)]
                            for i in xrange(self.chain_length)]
        
    def getSMatrix(self):
        return self._SMatrix
    
    def getPairs(self):
        self._buildSmatrix()
        return [(0,0)]
    
    def _buildSmatrix(self):
        for d in xrange(2, self.chain_length):
            i = 0
            for j in xrange(d, self.chain_length): 
                v = self._SMatrix[i+1][j-1] + self.energyMatrix[i][j]
                v = max(v, self._SMatrix[i+1][j])
                v = max(v, self._SMatrix[i][j-1])
                v = max([v] + [self._SMatrix[i][k] + self._SMatrix[k+1][j] for k in xrange(i+1,j)] )
                self.matrix[i][j] = v
                i += 1