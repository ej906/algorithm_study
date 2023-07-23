import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

t=int(input())

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(graph,x,y):
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    dfs(graph,nx,ny)



for _ in range(t):
    m,n,k=map(int,input().split())
    bachu=[[0]*(m) for _ in range(n)]
    
    for _ in range(k):
        y,x=map(int,input().split())
        bachu[x][y]=1
    
    cnt=0
    for a in range(n):
        for b in range(m):
            if bachu[a][b]==1:
                dfs(bachu,a,b)
                cnt+=1
    print(cnt)