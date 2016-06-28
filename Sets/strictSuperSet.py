#add all the sets to one big list and check for strict super set element by element
bigList = list()
result = True
a = set(map(int, raw_input().split()))
numberOfSetsToCheck = int(raw_input())
for x in range(numberOfSetsToCheck):
    b = set(map(int, raw_input().split()))
    bigList.append(b)
for item in bigList:
    if not a.issuperset(item):
        result = False
print result
