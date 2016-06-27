knapsack = set()
numPlants = int(raw_input())
sumOfLengths = 0
n = raw_input().split()
for item in n:
    knapsack.add(int(item))
#print knapsack
for plantLengths in knapsack:
    sumOfLengths = sumOfLengths + plantLengths
print "%.3f" % float(float(sumOfLengths)/float(len(knapsack)))


