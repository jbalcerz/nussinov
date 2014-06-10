'''
Created on Jun 10, 2014

@author: jerzy
'''
import sys
import src.nussinovMain as m

sys.tracebacklimit=0

if __name__ == '__main__':
    
    ret = m.main(sys.argv[1:])
    sys.exit(ret)
    
    pass