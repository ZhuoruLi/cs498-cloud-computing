#!/usr/bin/env python3
import sys
import re

leaguePath = sys.argv[1]
#TODO

league = []
with open(leaguePath) as f:
       for i in f.readlines():
              league.append(i.strip())
              
delimiters = "\\t|\\n"
pairDic = {} 
for line in sys.stdin:
       ids = re.split(delimiters, line.strip())
       pairDic[ids[0]] = ids[1]

for item in league:
       if item in pairDic:
              print('%s\t%s' % (item,pairDic[item]))
       #TODO

       # print('%s\t%s' % (  ,  )) pass this output to reducer
