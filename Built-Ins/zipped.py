#use of zip
data = raw_input()
sumOfScores = 0
finalList = list()
anotherList = list()
avgList = list()

first = list(int(i) for i in data.split())
numCourses = first[1]
numStudents = first[0]

for i in range(numCourses):
    finalList.append(raw_input().split())
anotherList = zip(*finalList)

for i in range(numStudents):
    for item in anotherList[i]:
        sumOfScores += float(item)
    avg = sumOfScores/numCourses
    avgList.append(avg)
    sumOfScores = 0
for item in avgList:
    print item
