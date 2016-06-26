M = int(raw_input())
setA = set(map(int, raw_input().split()))

N = int(raw_input())
setB = set(map(int, raw_input().split()))

for x in sorted(setA.symmetric_difference(setB)):
    print x