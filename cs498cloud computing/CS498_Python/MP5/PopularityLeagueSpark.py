#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
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

leagueIds = sc.textFile(sys.argv[2], 1)

leagueList = []
for league in leagueIds.collect():
    for pair in counts.collect():
        if int(league) == pair[0]:
            leagueList.append((league, pair[1]))
leagueList.sort(key = lambda x: (x[1], x[0]))

mini = 0
rank = {}
i = 0
while i < len(leagueList):
    if leagueList[i][1] >= mini:
        rank[leagueList[i][0]] = i
        mini = leagueList[i][1]
        i += 1
    # else:
    #     rank[leagueList[i][0]] = rank[leagueList[i-1][0]]
    #     i += 1
FinalRank = sorted(rank.items(),key = lambda x: (x[0]))

output = open(sys.argv[3], "w")
for item in FinalRank:
    output.write(str(item[0]) + "\t" + str(item[1]) + "\n")
#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

sc.stop()

