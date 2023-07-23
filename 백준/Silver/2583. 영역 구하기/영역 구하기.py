import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

m,n,k=map(int,input().split())
graph=[[0 for i in range(n)] for i in range(m)]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for a in range(x1,x2):
        for b in range(m-y2,m-y1):
            graph[b][a]=1

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def dfs(x,y):
    global cnt
    graph[x][y]=1
    cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                dfs(nx,ny)

count=[]
for a in range(m):
    for b in range(n):
        if graph[a][b]==0:
            cnt=0
            dfs(a,b)
            count.append(cnt)

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])