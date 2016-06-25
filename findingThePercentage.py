#done using text parsing
import sys
longString = str()
for line in sys.stdin:
    longString = longString + line.rstrip() + " "
lst = longString.split()
print lst
# #print 'Number of students', lst[0]
# numberOfStudents = lst[0]
posOfStudentOfInterest = 4*int(lst[0]) + 1
#print 'Student of interest', lst[posOfStudentOfInterest]
for item in lst:
    if item==lst[posOfStudentOfInterest]:
        score1 = lst[lst.index(item) + 1]
        score2 = lst[lst.index(item) + 2]
        score3 = lst[lst.index(item) + 3]
        break
avg = (float(score1)+float(score2)+float(score3))/3
print '{0:.2f}'.format(avg)