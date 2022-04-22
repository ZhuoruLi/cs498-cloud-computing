#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
#ret = []
d = {}
for line in sys.stdin:
    print(line)
    lower = line.strip().lower()
    if lower in d:
        d[lower] += 1
    else:
        d[lower] = 1
    # TODO
for item in d.items():
    #print(item)
    print('%s\t%s' % (item[0],item[1]))

# print('%s\t%s' % (  ,  )) print as final output
