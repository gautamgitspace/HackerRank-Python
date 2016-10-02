#!/usr/bin/env python
def missing_drone(drones):
    unique_id = 0
    for drone in drones:
        unique_id ^= int(drone)
    return unique_id
total_num = int(raw_input())
drones = raw_input().split()
print missing_drone(drones)
