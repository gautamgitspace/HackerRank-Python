lstC = list()
lst = list()
commands = int(raw_input())
for x in range (0,commands):
    command = raw_input()
    lstC = command.split()
    if lstC[0] == 'insert':
        lst.insert(int(lstC[1]), int(lstC[2]))
    elif lstC[0] == 'print':
        print lst
    elif lstC[0] == 'remove':
        lst.remove(int(lstC[1]))
    elif lstC[0] == 'append':
        lst.append(int(lstC[1]))
    elif lstC[0] == 'pop':
        lst.pop()
    elif lstC[0] == 'sort':
        lst.sort()
    elif lstC[0] == 'reverse':
        lst.reverse()

