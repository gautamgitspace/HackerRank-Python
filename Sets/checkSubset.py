for i in range(int(raw_input())):
    a = int(raw_input()); A = set(raw_input().split()); b = int(raw_input()); B = set(raw_input().split())
    if A.issubset(B): print True
    else: print False

# t = int(raw_input())
# for i in range(t):
#     num_a = int(raw_input())
#     a = set(raw_input().split())
#     num_b = int(raw_input())
#     b = set(raw_input().split())
#     if a.issubset(b):
#         print True
#     else:
#         print False