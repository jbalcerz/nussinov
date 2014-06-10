'''
Created on Jun 10, 2014

@author: jerzy
'''

import sys, os
lib_path = os.path.abspath('../src')
sys.path.append(lib_path)


import nussinovMain as m

sys.tracebacklimit=0

if __name__ == '__main__':
    
    ret = m.main(sys.argv[1:])
    sys.exit(ret)
    
    pass