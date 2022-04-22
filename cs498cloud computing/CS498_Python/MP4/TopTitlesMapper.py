#!/usr/bin/env python3
import sys
import re


# TODO
#mapperList = []
#ret = []
delimiters = "\\t|\\n"
pairList = []
for line in sys.stdin:
       pair = re.split(delimiters, line.strip())
       if len(pair) == 2:
              pair[1] = int(pair[1])
              pairList.append(pair)
for item in pairList:
       print('%s\t%s' % (item[0],item[1]))
#print(pairList[-5:])
       #mapperList.append(line)
#print(mapperList)
# ret = sorted(mapperList, key = lambda x: (x[1], x[0]))
# TenWords = ret[-5:]
# for item in TenWords:
#        print('%s\t%s' % (item[0],item[1]))
# print(TenWords)
       #TODO


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
