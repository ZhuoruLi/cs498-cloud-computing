#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import re
import statistics
import math

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

delimiters = "\\t|\\n"
lines = sc.textFile(sys.argv[1], 1)
numers = []
for line in lines.collect():
    splitStr = re.split(delimiters, line.strip())
    numers.append(int(splitStr[1]))
Sum = 0
for i in numers:
    Sum += i
    Mean = math.floor(Sum/len(numers))
Min = min(numers)
Max = max(numers)
Var = math.floor(statistics.pvariance(numers))
#TODO

outputFile = open(sys.argv[2], "w")
outputFile.write('Mean\t%s\n' % Mean)
outputFile.write('Sum\t%s\n' % Sum)
outputFile.write('Min\t%s\n' % Min)
outputFile.write('Max\t%s\n' % Max)
outputFile.write('Var\t%s\n' % Var)
'''
TODO write your output here
write results to output file. Format

'''
sc.stop()

