import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=[0]*(n+1)

for i in range(n):
    a[i+1]=int(input().strip())

coin=0
for i in range(n,0,-1):
    if k>=a[i]:
        coin+=k//a[i]
        k%=a[i]
    if k==0:
        break

print(coin)
        