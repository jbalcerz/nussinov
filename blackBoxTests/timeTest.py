'''
Created on Jun 10, 2014

@author: jerzy
'''
import sys, os
lib_path = os.path.abspath('../src')
sys.path.append(lib_path)
import nussinovMain as m

from timer import Timer


if __name__ == '__main__':
    with Timer() as t:
        ret = m.main(sys.argv[1:])
    
    print "=> elapsed time: %s s" % t.secs
    sys.exit(ret)

