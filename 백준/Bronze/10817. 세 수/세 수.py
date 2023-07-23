import sys
input=sys.stdin.readline().strip()

a_b_c=list(map(int,input.split()))
a_b_c.sort()

print(a_b_c[1])