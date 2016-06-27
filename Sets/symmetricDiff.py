sEng = set()
sFr = set()
count = 0
subscribersEng = int(raw_input())
rollNumbersEng = raw_input().split()
subscribersFr = int(raw_input())
rollNumbersFr = raw_input().split()
#print rollNumbersFr
for engReaders in rollNumbersEng:
    sEng.add(int(engReaders))
for frReadrers in rollNumbersFr:
    sFr.add(int(frReadrers))
for iterator in (sEng.symmetric_difference(sFr)):
    count = count + 1
print count