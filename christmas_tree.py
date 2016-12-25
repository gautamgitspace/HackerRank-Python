#!/usr/bin/env python
import time
def painttree(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x+=2
        z-=1
        time.sleep(0.2)
painttree(50)
