import sys
input=sys.stdin.readline

n=int(input())
road=list(map(int,input().strip().split()))
cost=list(map(int,input().strip().split()))

litter=0
for i in range(0,n-1):
    litter+=min(cost[:i+1])*road[i]

print(litter)
