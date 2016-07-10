#using namedtuple
from collections import namedtuple
count, Student = int(raw_input()), namedtuple('Student', raw_input().split())
students = []
for i in range(count):
    data = raw_input().split()
    students.append(Student(data[0], data[1], data[2], data[3]))
sum = 0
for student in students:
    sum += float(student.MARKS)
print (sum / float(count))