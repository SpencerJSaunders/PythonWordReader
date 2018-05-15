
import re
import string
import sys

#python .\main.py
#-1

argList = sys.argv 

file = open(argList[1])
d = {}


#each iteration is each line of the file
for line in file:
    for word in line.split():
      word = word.lower()
      word = re.sub(r'[^\w\s]','',word)

      if word:
          if word in d:
              d[word] += word.count(word)
          else:  
              d[word] = word.count(word)
              
a1_sorted_keys = sorted(d, key=d.get, reverse=True)
for r in a1_sorted_keys:
    print (r, d[r])

