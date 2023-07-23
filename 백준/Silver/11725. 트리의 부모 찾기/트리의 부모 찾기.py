import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent=[0]*(n+1)
visited=[0]*(n+1)

def dfs(start,visited):
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            parent[i]=start
            dfs(i,visited)

dfs(1,visited)
for i in range(2,n+1):
    print(parent[i])
    