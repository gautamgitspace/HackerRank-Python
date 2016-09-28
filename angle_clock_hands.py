#!/usr/bin/env python
#angle between the hands of a 12 hour analog clock at any given time in hours and minutes
def angle(hour, minute):
    angle = abs((hour * 30 + minute * 0.5)- (minute * 6))
    return min(angle, 360-angle)
hour = int(raw_input('Enter Hours '))
minute = int(raw_input('Enter Minutes '))
print str(angle(hour, minute)) + ' degrees'
