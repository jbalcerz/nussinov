'''
Created on May 26, 2014

@author: jerzy
'''
from numpy import matrix

class Nussinov(object):
    '''
    main algorithm implementation
    '''


    def __init__(self, chain, energyMatrix):
        '''
        Constructor
        '''
        self.chain = chain
        self.chain_length = len(chain)
        self._initialiseSmatrix()
        
    def _initialiseSmatrix(self):
        self.SMatrix = [(0,0)]
        
        
    def getPairs(self):
        '''
        Constructor
        '''
        return [(0,0)]
        
        
        
        
    def getSMatrix(self):
        '''
        Constructor
        '''