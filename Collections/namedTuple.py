#using namedtuple(STU)
from collections import namedtuple
count, STU = int(raw_input()), namedtuple('Student', raw_input().split())
students = []
for i in range(count):
    data = raw_input().split()
    students.append(STU(data[0], data[1], data[2], data[3]))
sum = 0
#print students
for iterator in students:
    #print iterator
    sum += float(iterator.MARKS)
print (sum / float(count))