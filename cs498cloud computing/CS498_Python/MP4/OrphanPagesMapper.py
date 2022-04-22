#!/usr/bin/env python3
import sys


for line in sys.stdin:
  #print(line)
  lines = line.split(":")
  print('%s\t%s' % (lines[0],lines[1]))
  # TODO
  
  # print('%s\t%s' % (  ,  )) pass this output to reducer
