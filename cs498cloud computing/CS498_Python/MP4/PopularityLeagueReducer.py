#!/usr/bin/env python3
import sys
import re
#TODO

# input comes from STDIN
delimiters = "\\t|\\n"
pairDic = {}
for line in sys.stdin:
    ids = re.split(delimiters, line.strip())
    pairDic[int(ids[0])] = int(ids[1])
popularity = sorted(pairDic.items(), key = lambda x: (x[1], x[0]))
mini = 0
rank = {}
i = 0
while i < len(popularity):
    if popularity[i][1] > mini:
        rank[popularity[i][0]] = i
        mini = popularity[i][1]
        i += 1
    else:
        rank[popularity[i][0]] = rank[popularity[i-1][0]]
        i += 1
FinalRank = sorted(rank.items(),key = lambda x: (-x[0]))
for items in FinalRank:
    print('%s\t%s' % (items[0], items[1]))
# for item in popularity:
#     if item[1] > minnum:
#         rank[item[0]] = i
#         i += 1
#     else:
#         rank[item[0]] = i
#         minnum = item[1]

    # TODO


#TODO
# print('%s\t%s' % (  ,  )) print as final output