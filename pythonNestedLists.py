lst = list()
uniqueListOfScores = list()
tempListOfScores = list()
pos = None
studentCount = int(raw_input())
lowest = None
for x in range(0,studentCount):
    lst.append([raw_input(), float(raw_input())])
#print lst
#print lst[0][1], lst[1][1], lst[2][1], lst[3][1], lst[4][1]

tempListOfScores = [lst[x][1] for x in range(0, studentCount)]
uniqueListOfScores = list(set(tempListOfScores))
minimumOfAll = min(uniqueListOfScores)
uniqueListOfScores.remove(minimumOfAll)
#print uniqueListOfScores
secondMinimumOfAll = min(uniqueListOfScores)
lst = [x[0] for x in lst if x[1] == secondMinimumOfAll]
#print lst
lst.sort()
if len(lst) > 1:
    print lst[0]
    print lst[1]
else:
    print lst[0]
