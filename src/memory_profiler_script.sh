#!/bin/sh

#  memory_profiler_script.sh
#  
#
#  Created by OLEG DRUZHYNETS on 06/06/14.
#

echo "Testing using memory profiler:" > memory_profiler_test.txt
python -m memory_profiler main.py -i sequences/1.txt -o output.txt >> memory_profiler_test.txt