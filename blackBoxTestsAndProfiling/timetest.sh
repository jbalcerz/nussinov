#!/bin/sh

#  timetest.sh
#
#
#  Created by OLEG DRUZHYNETS on 03/06/14.
#
#  Simple time test: measures the execution time of the program with given data and outputs results of the test to the file 'timetest.txt'.
#  WARNING: Any '@profile' lines in the program should be commented in order to complete this test

echo "Testing:" > timetest.txt
time python nussinovCall.py -i input.txt -o output.txt >> timetest.txt