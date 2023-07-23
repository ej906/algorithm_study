import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import copy

m,n=map(int,input().split())

box=[list(map(int,input().split())) for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

queue=deque()

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append([i,j])

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                queue.append([nx,ny])

for a in range(n):
    for b in range(m):
        if box[a][b]==0:
            print(-1)
            exit()

maximum=0
for i in range(n):
    maximum=max(maximum,max(box[i]))

print(maximum-1)