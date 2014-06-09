#!/usr/bin/env python
'''
    Created on May 25, 2014
    
    @author: jerzy
    '''

import sys
import nussinov, inputReader
import networkx as nx
import matplotlib.pyplot as plt
from timer import Timer

'''
    
    '''

def main(sys_arguments):
    try:
        data = inputReader.InputReader(sys_arguments)
    except inputReader.InputReaderException as er:
            print er
            return 1
    
    
    for chain in data:
        
        print 'input:', chain
        
        try:
            x = nussinov.Nussinov(chain,data.get_MinLoop(),data.get_EnergyMatrix())
            x.calculate()
            pairs = x.getPairs()
#             sMatrix = x.getSMatrix()

        except nussinov.NussinovException as er:
            print er
            data.closeFiles()
            return 1
            
        print 'output:', pairs
        
        (data.get_outputFileObject()).write(str(pairs) + '\n')
    
        G = nx.Graph()
        G.add_edges_from(pairs)
        nx.draw(G)
        plt.show()

    data.closeFiles()
    return 0


if __name__ == '__main__':
    
#     sys.tracebacklimit=0
    with Timer() as t:
        ret = main(sys.argv[1:])
       
    print "=> elapsed time: %s s" % t.secs
    sys.exit(ret)

           

 
 
 
