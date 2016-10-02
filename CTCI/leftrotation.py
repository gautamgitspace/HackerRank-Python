#!/usr/bin/env python
def array_left_rotation(a, n, k):
    temp = []
    for item in range(n):
        temp.append(a[(item+k)%n])
    return temp


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
