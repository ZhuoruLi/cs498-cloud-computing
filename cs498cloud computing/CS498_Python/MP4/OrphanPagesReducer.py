#!/usr/bin/env python3
import sys
import re

#TODO
startID = {}
endID = {}
delimiters = "\\t|\\n"
for line in sys.stdin:
  lines = re.split(delimiters, line.strip())
  startID[lines[0].strip()] = 0
  if len(lines) == 2:
    splitDes = lines[1].split(" ")
    for i in splitDes:
      if i and i != lines[0]:
        endID[i.strip()] = 1

output = []
for ID in startID:
  if ID not in endID:
    if ID:
      output.append(int(ID))
sortedList = sorted(output)
for item in sortedList:
  print(item)



  # TODO

#TODO
# print(xx) print as final output