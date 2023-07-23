import sys
n,m=map(int,input().split())
num=[0]*n
for a in range(m):
    i,j,k=map(int,sys.stdin.readline().split())
    for b in range(i-1,j):
        num[b]=k

for i in range(n):
    print(num[i],end=' ')