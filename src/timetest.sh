#!/bin/sh

#  line_profiler_script.sh
#
#
#  Created by OLEG DRUZHYNETS on 03/06/14.
#

echo "Testing on 10 sequences:" > timetest.txt
echo "1st sequence:" >> timetest.txt
time python main.py -i sequences/1.txt -o out1.txt >> timetest.txt
echo "2nd sequence:" >> timetest.txt
time python main.py -i sequences/2.txt -o out2.txt >> timetest.txt
echo "3rd sequence:" >> timetest.txt
time python main.py -i sequences/3.txt -o out3.txt >> timetest.txt
echo "4th sequence:" >> timetest.txt
time python main.py -i sequences/4.txt -o out4.txt >> timetest.txt
echo "5th sequence:" >> timetest.txt
time python main.py -i sequences/5.txt -o out5.txt >> timetest.txt
echo "6th sequence:" >> timetest.txt
time python main.py -i sequences/6.txt -o out6.txt >> timetest.txt
echo "7th sequence:" >> timetest.txt
time python main.py -i sequences/7.txt -o out7.txt >> timetest.txt
echo "8th sequence:" >> timetest.txt
time python main.py -i sequences/8.txt -o out8.txt >> timetest.txt
echo "9th sequence:" >> timetest.txt
time python main.py -i sequences/9.txt -o out9.txt >> timetest.txt
echo "10th sequence:" >> timetest.txt
time python main.py -i sequences/10.txt -o out10.txt >> timetest.txt
