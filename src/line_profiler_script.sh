#!/bin/sh

#  line_profiler_script.sh
#  
#
#  Created by OLEG DRUZHYNETS on 03/06/14.
#

echo "Testing using line-to-line profiler:" > line_profiler_test.txt
kernprof.py -l -v main.py -i sequences/1.txt -o output.txt >> line_profiler_test.txt