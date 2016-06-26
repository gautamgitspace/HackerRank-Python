lst = list()
unqlst = list()
n = int(raw_input())
l = raw_input()
for x in l.split():
    lst.append(int(x))
lst.sort()
unqlst = list(set(lst))
maxOfAll = max(unqlst)
unqlst.remove(maxOfAll)
print max(unqlst)

