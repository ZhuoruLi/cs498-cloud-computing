#!/usr/bin/env python3

import sys
import string
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

# TODO
stopWords = []
with open(stopWordsPath) as f:
    for word in f.readlines():
        stopWords.append(word.strip())
         # TODO
#print(stopWords)

#  	,;.?!-:@[](){}_*/
#delimiters = r'[ ,;.?!-:@[](){}_*/]'
delimiters = "\\t|,|;|\\.|\\?|!|-|:|@|[|]|\\(|\\)|{|}|_|\\*|/"
#delimiters = "[\s+,;\.\?\!\-\:@\[\]\(\)\{\}_(?:(?!/)(?:.|\n))*/]"
# with open(delimitersPath) as f:
   
    # TODO

for line in sys.stdin:
    targetList = re.split(delimiters, line.strip())
    # TODO
    for item in targetList:
        if item.lower() not in stopWords and item:
            print(item.lower())
            #print('%s\t%s' % (  ,  ))
    #  
#pass this output to reducer


