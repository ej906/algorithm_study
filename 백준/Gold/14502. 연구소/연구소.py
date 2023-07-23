import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy

#연구소

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs():
    graph_c=copy.deepcopy(graph)
    queue=deque()
    for i in range(n):
        for j in range(m):
            if graph_c[i][j]==2:
                queue.append((i,j))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph_c[nx][ny]==0:
                    queue.append((nx,ny))
                    graph_c[nx][ny]=2
    global result
    cnt=0
    for i in range(n):
        cnt+=graph_c[i].count(0)
    result=max(result,cnt)

def three_choose(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                three_choose(cnt+1)
                graph[i][j]=0

result=0
three_choose(0) 
print(result)
