import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

n,m = map(int,input().split())

graph=[[]for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
  
def dfs(graph,start,visited):
    visited[start]=1
    for i in graph[start]:
        if visited[i]!=1:
            dfs(graph,i,visited)

visited=[0]*(n+1)
cnt=0
for i in range(1,n+1):
    if visited[i]!=1 :
        cnt+=1
        dfs(graph,i,visited)

print(cnt)