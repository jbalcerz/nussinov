#!/bin/sh

#  line_profiler_script.sh
#  
#
#  Created by OLEG DRUZHYNETS on 03/06/14.
#
#  We use Robert Kern's line_profiler in order to see how fast and how often each line of code is running in our scripts. In order to use it, we needed to install the python package via pip:
#                       $ pip install line_profiler
#  Once installed we have access to a new module called “line_profiler” as well as an executable script “kernprof.py”.
#  In order to use this tool, we modify our source code by decorating the function we want to measure with the @profile decorator. We didn’t have to import anything in order to use this decorator. The kernprof.py script automatically injects it into our script’s runtime during execution.
#  Once we’ve gotten our code setup with the @profile decorator, the kernprof.py is being used to run our script:
#                      $ kernprof.py -l -v main.py
#  The -l option tells kernprof to inject the @profile decorator into our script’s builtins, and -v tells kernprof to display timing information once our script finishes.
#  Results of the test are being written to 'line_profiler_test.txt' file.
#  Look for lines with a high amount of hits or a high time interval. These are the areas where optimizations can yield the greatest improvements.

echo "Testing using line-to-line profiler:" > line_profiler_test.txt
kernprof.py -l -v main.py -i sequences/1.txt -o output.txt >> line_profiler_test.txt