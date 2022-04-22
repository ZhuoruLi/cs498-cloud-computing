#!/usr/bin/env python3
import sys
import math
import re
import statistics
#TODO
receivedline = []
delimiters = "\\t|\\n"
for line in sys.stdin:
    figures = re.split(delimiters, line.strip())
    receivedline.append(int(figures[0]))
# print(receivedline)
nameList = ["Mean", "Sum", "Min", "Max", "Var"]
Sum = 0
for i in receivedline:
    Sum += i
Mean = math.floor(Sum/len(receivedline))
Min = min(receivedline)
Max = max(receivedline)
# Var = 0
# for number in receivedline:
#     Var += math.floor((number - Mean)**2/len(receivedline))
Var = math.floor(statistics.pvariance(receivedline))
figureList = [Mean, Sum, Min, Max, Var]
pairList = []
for i in range(len(nameList)):
    pair = (nameList[i], figureList[i])
    pairList.append(pair)
for item in pairList:
    print('%s\t%s' % (item[0],item[1]))
#     # TODO

#TODO
# print('%s\t%s' % (  ,  )) print as final output
