s = set()
numberOfElements = int(raw_input())
elements = raw_input().split()
for item in elements:
    s.add(int(item))
#print s
commands = int(raw_input())
for x in range(commands):
    command = raw_input().split()
    if command[0] == 'pop':
        s.pop()
        #print s
        #print 'done popping'
    elif command[0] == 'remove':
        s.remove(int(command[1]))
        #print s
        #print 'done removing'
    elif command[0] == 'discard':
        s.discard(int(command[1]))
        #print s
        #print 'done discarding'
print sum(s)
