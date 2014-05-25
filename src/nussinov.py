#!/usr/bin/env python
'''
Created on May 25, 2014

@author: jerzy
'''

# just to play with unit tests
def IsOdd(n):
    return n % 2 == 1


class Foo:

    def __init__(self):
        self.foo = 10
        print(self.foo)


if __name__ == '__main__':
    Foo()