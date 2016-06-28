num_a = raw_input()
a = set(map(int, raw_input().split()))
n = int(raw_input())
 
for i in range(n):
	command = raw_input().split()
	b = set(map(int, raw_input().split()))

	if command[0] == "update":
		a.update(b)
	elif command[0] == "intersection_update":
		a.intersection_update(b)
	elif command[0] == "difference_update":
		a.difference_update(b)
	elif command[0] == "symmetric_difference_update":
		a.symmetric_difference_update(b)

print sum(a)