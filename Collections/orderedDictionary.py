#using orderedDictionaries
from collections import OrderedDict
items = int(raw_input())
d = OrderedDict()
for i in range(items):
    itemName, itemPrice = raw_input().rsplit(' ', 1)
    if itemName not in d:
        d[itemName] = int(itemPrice)
    else:
        d[itemName] += int(itemPrice)
for i, j in d.items():
    print str(i), str(j)
