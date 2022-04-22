#!/usr/bin/env python3
import sys
import re

# bigFive = []
# result = []
pairList = []
delimiters = "\\t|\\n"
for line in sys.stdin:
    pair = re.split(delimiters, line.strip())
    if len(pair) == 2:
        pair[1] = int(pair[1])
        pairList.append(pair)
pairList.sort(key = lambda x: (x[1], x[0]))
for item in pairList[-10:]:
    print('%s\t%s' % (item[0],item[1]))
    #print(line)
    # fifth = line[-1]
    # bigFive.append(fifth)
# result = sorted(bigFive, key = lambda x: (x[1], x[0]))
# finalFive = result[-5:]
# for items in finalFive:
#         print('%s\t%s' % (items[0],items[1]))
    # TODO
    
    # print('%s\t%s' % (  ,  )) print as final output