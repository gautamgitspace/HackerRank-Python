import textwrap
data = raw_input()
width = int(raw_input())
lst = textwrap.wrap(data, width)
for item in lst:
    print item