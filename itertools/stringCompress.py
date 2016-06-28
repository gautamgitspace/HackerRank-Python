from itertools import groupby
s = raw_input()
for key, group in groupby(s):
    print (len(list(group)), int(key))
