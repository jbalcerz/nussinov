#!/bin/sh

#  timetest.sh
#
#
#  Created by OLEG DRUZHYNETS on 03/06/14.
#
#  Simple time test: measures the execution time of the program with given data and outputs results of the test to the file 'timetest.txt'.
#  WARNING: Any '@profile' lines in the program should be commented in order to complete this test

if [ "$1" == "" ]
then
    echo "You need to pass the nussinovCalculator.py file path and its arguments"
    exit 1
fi
echo "Testing:" > blackBoxTestsAndProfiling/timetest.txt
time python "$1" >> blackBoxTestsAndProfiling/timetest.txt

