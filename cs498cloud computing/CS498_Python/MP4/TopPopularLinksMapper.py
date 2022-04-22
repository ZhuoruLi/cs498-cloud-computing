#!/usr/bin/env python3
import sys
import re

# TODO


delimiters = "\\t|\\n"
pairList = []
for line in sys.stdin:
       pair = re.split(delimiters, line.strip())
       pair[1] = int(pair[1])
       pairList.append(pair)            
for item in pairList:
       print('%s\t%s' % (item[0],item[1]))
       #TODO


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
