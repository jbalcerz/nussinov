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

    chain = 'CCCAAAAGGG'
    print 'input:', chain, '\n'
    energyMatrix = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
     
    #main algorithm
    x = nussinov.Nussinov(chain,energyMatrix)
    x.calculate()
    pairs = x.getPairs()
    sMatrix = x.getSMatrix()
    
    print 'output:', pairs, '\n'
    
    #some output formatting
#    out = OutputWriter(chain,pairs,sMatrix)
    
 
 
 
