#from __future__ import print_function
from itertools import combinations_with_replacement
data = raw_input().split()
word = data[0]
word = sorted(word)
parameter = int(data[1])
#print word
#print parameter
l = map("".join, list(combinations_with_replacement(word, parameter)))
for item in sorted(l):
        print item