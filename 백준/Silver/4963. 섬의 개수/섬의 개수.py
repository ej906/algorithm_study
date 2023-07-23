import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


dx=[0,1,0,-1,1,1,-1,-1]
dy=[1,0,-1,0,1,-1,1,-1]

def dfs(x,y):
    island[x][y]=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx and nx<h and 0<=ny and ny<w:
            if island[nx][ny] == 1:
                dfs(nx,ny)

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break 
    island=[]
    
    for _ in range(h):
        island.append(list(map(int,input().strip().split())))
    cnt=0
    for a in range(h):
        for b in range(w):
            if island[a][b]==1:
                dfs(a,b)
                cnt+=1
    
    print(cnt)
