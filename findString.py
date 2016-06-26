#IMP - number of comparisons are equal to big len - small len + 1 (here it is - lenusable)
big = raw_input()
small = raw_input()
len1 = len(big)
len2 = len(small)
count = 0
lenusable = len1-len2+1
#print lenusable
for x in range(0, lenusable):
    if big[x:x+len2] == small:
        count = count+1
print count
