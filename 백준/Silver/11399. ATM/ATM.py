import sys
input=sys.stdin.readline

n=int(input())

p=list(map(int,input().split()))

p.sort()
p_sum=[0]*n
p_sum[0]=p[0]

for i in range(1,n):
    p_sum[i]=p[i]+p_sum[i-1]

print(sum(p_sum))