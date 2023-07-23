import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n=int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y):
    land_1[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n: 
            if land_1[nx][ny]==1:
                dfs(nx,ny)

land=[]
height=[0]

for i in range(n):
    land.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if land[i][j] not in height:
            height.append(land[i][j])

land_1= [[0]*n for _ in range(n)]
count=[]
for i in height:
    for a in range(n):
        for b in range(n):
            if land[a][b]>i:
                land_1[a][b]=1
    cnt=0
    for a in range(n):
        for b in range(n):
            if land_1[a][b]==1:
                dfs(a,b)
                cnt+=1
    count.append(cnt)

print(max(count))