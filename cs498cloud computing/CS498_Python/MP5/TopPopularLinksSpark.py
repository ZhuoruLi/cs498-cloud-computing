#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

def findFirst(word):
  if word.find(":") != -1:
    otherword = word[:-1]
    return (int(otherword), 0)
  else:
    return (int(word), 1)
counts = lines.flatMap(lambda line: line.split(" ")) \
             .map(findFirst) \
             .reduceByKey(lambda a, b: a + b).filter(lambda x : int(x[1])!=0)

output = open(sys.argv[2], "w")
outputList = []
for item in counts.takeOrdered(10, key=lambda x: -x[1]):
    outputList.append(item)
stringList = []
for stringItem in outputList:
    stringList.append((str(stringItem[0]), stringItem[1]))
stringList.sort(key=lambda x:x[0])
stringList.reverse()
while len(stringList) != 0:
    other = stringList.pop()
    output.write(str(other[0]) + "\t" + str(other[1]) + "\n")


#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

sc.stop()

