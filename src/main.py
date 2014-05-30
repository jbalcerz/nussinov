#!/usr/bin/env python
'''
Created on May 25, 2014

@author: jerzy
'''

import sys
import nussinov
import inputReader
from inputReader import InputReaderException

'''

'''

if __name__ == '__main__':

#     sys.tracebacklimit=0
    try:
        receivedChains = inputReader.InputReader(sys.argv[1:])
    except InputReaderException as er:
        print er
        try:
            receivedChains
        except NameError:
            pass
        else:
            receivedChains.closeFiles()
            sys.exit(2)
           
       
    
    for chain in receivedChains:
        
        print 'input:', chain
        
        energyMatrix = [[0,0,0,2],[0,0,3,0],[0,3,0,3],[2,0,1,0]]
        x = nussinov.Nussinov(chain,energyMatrix)
        x.calculate()
        pairs = x.getPairs()
        sMatrix = x.getSMatrix()
            
        print 'output:', pairs
        
        (receivedChains.get_outputFileObject()).write(str(pairs) + '\n')
        
    
    receivedChains.closeFiles()
    sys.exit(0)
           

 
 
 
