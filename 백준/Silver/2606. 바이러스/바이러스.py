import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

m=int(input())

network=[[]for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=1
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]!=1:
                visited[i]=1
                queue.append(i)
                
visited=[0]*(n+1)
bfs(network,1,visited)
print(visited.count(1)-1)