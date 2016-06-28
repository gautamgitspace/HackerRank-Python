#from __future__ import print_function
from itertools import permutations
data = raw_input().split()
word = data[0]
parameter = int(data[1])
print word
print parameter
b = list(permutations(word, parameter))
for item in sorted(b):
    print("".join(item))