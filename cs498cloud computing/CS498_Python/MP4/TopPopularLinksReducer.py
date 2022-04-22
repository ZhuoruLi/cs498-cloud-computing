#!/usr/bin/env python3
import sys
import re

pairList = []
delimiters = "\\t|\\n"
# input comes from STDIN
for line in sys.stdin:
    pair = re.split(delimiters, line.strip())
    pair[1] = int(pair[1])
    pairList.append(pair)

pairList.sort(key = lambda x: (x[1], x[0]))
for item in pairList[-10:]:
    print('%s\t%s' % (item[0],item[1]))
    # TODO
    # print('%s\t%s' % (  ,  )) print as final output
