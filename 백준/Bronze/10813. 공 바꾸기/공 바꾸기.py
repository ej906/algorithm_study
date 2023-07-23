import sys
n,m=map(int,input().split())
num=[0]*(n+1)
for i in range(1,n+1):
    num[i]=i

for k in range(m):
    i,j=map(int,sys.stdin.readline().split())
    num[i],num[j]=num[j],num[i]

for i in range(1,n+1):
    print(num[i],end=' ')
