# *IMP* - can't append to tuple, so append to a list instead and later cast into a tuple
lst = list()
n = int(raw_input())
l = raw_input()
for x in l.split():
    lst.append(int(x))
t = tuple(lst)
print hash(t)