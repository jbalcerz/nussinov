#!/usr/bin/env python
'''
Created on May 25, 2014

@author: jerzy
'''


def IsOdd(n):
    """
     function just to play with unit tests
    """
    return n % 2 == 1


class DatePattern:
    """    
     class just to play with unit tests
    """
    def __init__(self, year, month, day):
        self.year  = year
        self.month = month
        self.day   = day
    
    def matches(self, date):
        return ((self.year  and self.year  == date.year  or True) and
                (self.month and self.month == date.month or True) and
                self.day == date.day)

if __name__ == '__main__':
    print "hello world"