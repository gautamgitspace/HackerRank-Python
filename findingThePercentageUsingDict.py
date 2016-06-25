#done using dictionaries taking raw_input line by line
numberOfStudents = int(raw_input())
total = dict()
for i in range(0, numberOfStudents):
    tokens = raw_input().split()
    name = tokens[0]
    total[name] = float(tokens[1]) + float(tokens[2]) + float(tokens[3])
student = raw_input()
print "{0:.2f}".format(total[student] / 3)