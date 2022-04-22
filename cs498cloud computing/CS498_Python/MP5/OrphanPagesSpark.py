#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import string
#import re

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

# startID = {}
# endID = {}
# # delimiters = "\\t|\\n"
lines = sc.textFile(sys.argv[1], 1) 
  
def findFirst(word):
  if word.find(":") != -1:
    otherword = word[:-1]
    return (int(otherword), 0)
  else:
    return (int(word), 1)
counts = lines.flatMap(lambda line: line.split(" ")) \
             .map(findFirst) \
             .reduceByKey(lambda a, b: a + b).filter(lambda x : int(x[1])==0)

output = open(sys.argv[2], "w")
for item in counts.sortBy(lambda x: str(x[0])).collect():
  output.write(str(item[0]) + "\n")

sc.stop()
# for line in lines.collectAsMap():
#     splitStr = line.split(":")
#     startID[splitStr[0].strip()] = 0
#     if len(splitStr == 2):
#         splitDes = splitStr[1].split(" ")
#         for i in splitDes:
#             if i and i != splitStr[0]:
#                 endID[i.strip()] = 1

# output = []
# for ID in startID:
#   if ID not in endID:
#     if ID:
#       output.append(int(ID))
# sortedList = sorted(output)
# #TODO

# output = open(sys.argv[2], "w")
# for item in sortedList:
#   output.write(item + "\n")
#TODO
#write results to output file. Foramt for each line: (line + "\n")



