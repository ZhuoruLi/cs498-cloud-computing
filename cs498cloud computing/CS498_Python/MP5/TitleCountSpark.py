#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
import re
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopWords = []
with open(stopWordsPath) as f:
    for word in f.readlines():
        stopWords.append(word.strip())
 #TODO

# with open(delimitersPath) as f:
#     #TODO
delimiters = "\\t|,|;|\\.|\\?|!|-|:|@|[|]|\\(|\\)|{|}|_|\\*|/"

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)
lowerTitle = []
for line in lines.collect():
    targetList = re.split(delimiters, line.strip())
    # TODO
    for item in targetList:
        if item.lower() not in stopWords and item:
            lowerTitle.append(item.lower())
d = {}
for Title in lowerTitle:
    if Title in d:
        d[Title] += 1
    else:
        d[Title] = 1
SortedTitle = sorted(d.items(), key = lambda x: x[1])
tenWord = SortedTitle[-10:]
tenWord.sort(key = lambda x: x[0])
outputFile = open(sys.argv[4],"w")
for item in tenWord:
    outputFile.write(item[0] + "\t" + str(item[1]) + "\n")
#TODO
#write results to output file. Foramt for each line: (line +"\n")
sc.stop()