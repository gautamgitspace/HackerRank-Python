#use of sorted, key and lambda
rows, cols = map(int, raw_input().split())
lst = list()
sortedList = list()
for iterator in range(rows):
    lst.append(map(int, raw_input().split()))
k = int(raw_input())
sortedList = sorted(lst, key=lambda x: x[k])
for item in sortedList:
    print " ".join(map(str, item))