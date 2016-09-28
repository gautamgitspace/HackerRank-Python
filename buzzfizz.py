#!/usr/bin/env python
def bark():
    for x in range(0, 100):
        if(x % 5 == 0):
            print str(x) + ' Buzz'
        if(x % 3 ==0):
            print str(x) + ' Fizz'
bark()
