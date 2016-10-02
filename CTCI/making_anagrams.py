#!/usr/bin/env python
from collections import Counter
def diff(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    count_a.subtract(count_b)
    return sum(abs(k) for k in count_a.values())

a = raw_input('Enter first string: ').strip()
b = raw_input('Enter second string: ').strip()

number = diff(a, b)
if number == 0:
    print 'Stupid. You entered two anagrams'
else:
    print number, 'chars need to deleted'
