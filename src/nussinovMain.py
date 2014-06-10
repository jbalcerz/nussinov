#!/usr/bin/env python
'''
    Created on May 25, 2014
    
    @author: jerzy
    '''

import sys
import nussinov as nus
import inputReader as iR
import networkx as nx
import matplotlib.pyplot as plt


def main(sys_arguments):
    
    try:
        data = iR.InputReader(sys_arguments)
    except iR.InputReaderException as er:
            print er
            return 1
    
    for chain in data:
        print 'input:', chain
        
        try:
            x = nus.Nussinov(chain,data.get_MinLoop(),data.get_EnergyMatrix())
            x.calculate()
            pairs = x.getPairs()
#             sMatrix = x.getSMatrix()

        except nus.NussinovException as er:
            print er
            data.closeFiles()
            return 1
            
        print 'output:', pairs
        
#       any exepitons chatching here??
        (data.get_outputFileObject()).write(str(pairs) + '\n')
        visualisation(chain,pairs)

    data.closeFiles()
    return 0

def visualisation(chain,pairs):
        G = nx.Graph()
        
        a = range(len(chain))
        G.add_edges_from([(i,i+1) for i in a[:-1]])
        
        G.add_edges_from(pairs)
        nx.draw(G)
        plt.show()
        
        
        
if __name__ == '__main__':
    ret = main(sys.argv[1:])
    sys.exit(ret)
    

           

 
 
 
