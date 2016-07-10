from collections import Counter
items = int(raw_input())
sizes = Counter(map(int, raw_input().split()))
#print sizes
customerCount = int(raw_input())
rate = []
for i in range(customerCount):
    rate.append(map(int, raw_input().split()))
#print rate
earnings = 0
for item in rate:
    if sizes[item[0]] > 0:
        earnings += item[1]
        sizes[item[0]] -= 1
print earnings

