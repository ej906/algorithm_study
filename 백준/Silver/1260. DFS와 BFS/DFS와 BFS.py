import sys
from collections import deque
input=sys.stdin.readline

n,m,v=map(int,input().split())
graph=[[]for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


def dfs(graph,start,visited):
    visited[start]=1
    print(start,end=' ')
    for i in graph[start]:
        if visited[i]!=1:
            dfs(graph,i,visited)


def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=1
    while queue:
        p=queue.popleft()
        print(p,end=' ')
        for i in graph[p]:
            if visited[i]!=1:
                visited[i]=1
                queue.append(i)


visited_1=[0]*(n+1)
dfs(graph,v,visited_1)
print()

visited_2=[0]*(n+1)
bfs(graph,v,visited_2)