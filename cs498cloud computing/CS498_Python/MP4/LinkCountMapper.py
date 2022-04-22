#!/usr/bin/env python3
import sys


for line in sys.stdin:
  idList = line.split(":")[1]
  desList = idList.split(" ")
  for ID in desList:
    if ID:
      print('%s\t%s' % (ID.strip(),1))


  #TODO

  # print('%s\t%s' % (  ,  )) pass this output to reducer
