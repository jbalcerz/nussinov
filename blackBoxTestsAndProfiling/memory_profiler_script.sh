#!/bin/sh

#  memory_profiler_script.sh
#  
#
#  Created by OLEG DRUZHYNETS on 06/06/14.
#
#  We are using this test in order to figure out how much memory our program is using. Fortunately for us, Fabian Pedregosa has implemented a nice memory profiler modeled after Robert Kern’s line_profiler.
#  In order to use it, we install it via pip:
#                    $ pip install -U memory_profiler
#                         $ pip install psutil
# (Installing the psutil package here is recommended because it greatly improves the performance of the memory_profiler).
# Like line_profiler, memory_profiler requires that we decorate our function of interest with an @profile decorator.
# Results of the test are being saved to the 'memory_profile_test.txt' file.

echo "Testing using memory profiler:" > memory_profiler_test.txt
python -m memory_profiler main.py -i sequences/1.txt -o output.txt >> memory_profiler_test.txt
