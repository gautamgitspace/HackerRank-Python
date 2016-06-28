t = int(raw_input())
for i in range(t):
    num_a = int(raw_input())
    a = set(raw_input().split())
    num_b = int(raw_input())
    b = set(raw_input().split())
    if a.issubset(b):
        print True
    else:
        print False