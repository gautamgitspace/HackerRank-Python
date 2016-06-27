stamps = set()
numberOfStamps = int(raw_input())
for x in range(numberOfStamps):
    country = raw_input().rstrip()
    stamps.add(country)
print len(stamps)