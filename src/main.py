#!/usr/bin/env python
'''
Created on May 25, 2014

@author: jerzy
'''


import nussinov
import inputReader
import outputWriter

if __name__ == '__main__':

#   here should be called inputReader somehow like: 
#   chain = inputReader()
    chain = 'GGGAAAACCC'
    
    """
    example energy matrix:
    
    e(i,j) A C G U
    A      0 0 0 2
    C      0 0 3 0
    G      0 3 0 3
    U      2 0 1 0
    """
    energyMatrix = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
     
     
    #main algorithm
    x = nussinov.Nussinov(chain,energyMatrix)
    pairs = x.getPairs();
    sMatrix = x.getSMatrix(); 
     
    #some output formatting
#     out = OutputWriter(chain,pairs,sMatrix)
    
 
 
 
