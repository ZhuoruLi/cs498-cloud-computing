#!/usr/bin/env python3
import sys
import re
delimiters = "\\t|\\n"
# figures = []
for line in sys.stdin:
    figure = re.split(delimiters, line.strip())[1]
    #figures.append(figure)
    print('%s\t%s' % (figure,0))
#nameList = ["Mean", "Sum", "Min", "Max", "Var"]
    # TODO
    
    #  pass this output to reducer
