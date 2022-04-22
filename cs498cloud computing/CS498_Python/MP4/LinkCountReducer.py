#!/usr/bin/env python3
import sys
import re
#TODO

# input comes from STDIN
d = {}
delimiter = "\\t|\\n"
for line in sys.stdin:
    pairList = re.split(delimiter, line.strip())
    if int(pairList[0]) in d:
        d[int(pairList[0])] += 1
    else:
        d[int(pairList[0])] = 1
    # TODO
for item in d.items():
    print('%s\t%s' % (item[0],item[1]))
# TODO
# print('%s\t%s' % (  ,  )) print as final output