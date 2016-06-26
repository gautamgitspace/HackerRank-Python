input = raw_input()
l = list()
outputStr = str()
for alphabet in input:
    l.append(alphabet)
nextInput = raw_input()
nextInputSplit =  nextInput.split()
l[int(nextInputSplit[0])]=nextInputSplit[1]
for iterator in l:
    outputStr =  outputStr + iterator
print outputStr
