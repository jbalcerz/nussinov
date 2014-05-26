'''
Created on May 26, 2014

@author: jerzy
'''

class InputReader(object):
    '''
        Let's make a nice class to encapsulate some methods with "_" sign.
        
        The input should be handeled here. What should it do:
        - display prompt to the user 
        - read data from keyboard (one line)...
        - or ask use for a path and read data form file
        - check if data is correct (letters in sequence ok?)
        - to the main procedute I want to receive a string containing symbols 
        form group {ACGU} 
           
        what to add later:
        - should we read energy matrix form user?
        - should we read the smallest noumber of elements in a loop? 
          (compare pages 43 and 48 in Nowak's lecture notes)
        - in case of reading from file: maybe read each line of file as separate 
          chain and make it possible to iterate through them?
        - read data form RNA STRAND database - it is actual database that you 
          can download (around 30MB) form http://www.rnasoft.ca/strand/ 
          using this would be really nice! 
          (watch out - there is a special formatting and more than 4 symbols in chains)
        
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
        