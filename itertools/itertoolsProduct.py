str1 = str()
from itertools import product
lstA = map(int, raw_input().split())
lstB = map(int, raw_input().split())
print ' '.join(map(str,list(product(lstA, lstB))))