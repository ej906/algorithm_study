import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#치킨배달 문제

n,m=map(int,input().split())

city=[list(map(int,input().split())) for _ in range(n)]

chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==2:
            chicken.append((i,j))
        elif city[i][j]==1:
            house.append((i,j))
result=20000
for chi in combinations(chicken,m):
    sum=0
    for i in house:
        min_len=999
        x,y=i
        for j in range(m):
            min_len=min(min_len,abs(chi[j][0]-x)+abs(chi[j][1]-y))
        sum+=min_len
    result=min(result,sum)

print(result)
