#!/usr/bin/env python
'''
Created on May 25, 2014

@author: jerzy
'''

import sys
import nussinov
import inputReader
# import outputWriter

if __name__ == '__main__':

    receivedChains = inputReader.InputReader(sys.argv[1:])
    
    for chain in receivedChains:
        
        print 'input:', chain
        
        energyMatrix = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
        x = nussinov.Nussinov(chain,energyMatrix)
        x.calculate()
        pairs = x.getPairs()
        sMatrix = x.getSMatrix()
            
        print 'output:', pairs, '\n'
    

    #TODO: obsluga wyjscia
 
 
 
