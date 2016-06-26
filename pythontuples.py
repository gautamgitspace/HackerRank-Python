# *IMP* - creating a tuple using for loop
lst = list()
n = int(raw_input())
l = raw_input()
for x in l.split():
    lst.append(int(x))
t = tuple(lst)
print hash(t)