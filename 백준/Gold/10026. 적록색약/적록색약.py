import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 4)
import copy

n=int(input())

graph1=[]
for i in range(n):
    graph1.append(list(input().strip()))

graph2 = copy.deepcopy(graph1)#적록색약 그래프

for i in range(n):
    for j in range(n):
        if graph2[i][j]=='G':
            graph2[i][j]='R'

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(graph,x,y,color): #정상 사람인 경우
    graph[x][y]=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if graph[nx][ny]==color:
                dfs(graph,nx,ny,color)

cnt1=0
cnt2=0

for a in range(n):
    for b in range(n):
        if graph1[a][b]!=0:
            dfs(graph1,a,b,graph1[a][b])
            cnt1+=1

for a in range(n):
    for b in range(n):
        if graph2[a][b]!=0:
            dfs(graph2,a,b,graph2[a][b])
            cnt2+=1

print(cnt1, cnt2)