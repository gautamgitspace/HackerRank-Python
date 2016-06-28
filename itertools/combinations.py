#from __future__ import print_function
from itertools import combinations
data = raw_input().split()
word = data[0]
word = sorted(word)
parameter = int(data[1])
#print word
#print parameter
for i in range(1, parameter+1):
    l = map("".join, list(combinations(word, i)))
    for item in sorted(l):
        print item