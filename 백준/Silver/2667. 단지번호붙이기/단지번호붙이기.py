import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
apart=[[]for i in range(n)]
for i in range(n):
    apart[i]=list(map(int,input().strip()))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(graph,start_x,start_y):
    if start_x<0 or n<=start_x or start_y<0 or n<=start_y:
        return False
    if graph[start_x][start_y]!=0:
        graph[start_x][start_y]=0
        global count
        count+=1
        for i in range(4):
            x=start_x+dx[i]
            y=start_y+dy[i]
            dfs(graph,x,y)
        return True
    else:
        return False
      
cnt=[]
count=0
for i in range(n):
    for j in range(n):
        if dfs(apart,i,j) == True:
            cnt.append(count)
            count=0

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)

