import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
k=int(input())

board=[[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x,y=map(int,input().split())
    board[x-1][y-1]=1

L=int(input())
go_list=[]
#시계방향
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(L):
    x,c=map(str,input().split())
    go_list.append((int(x),c))


time,i=0,0
nd,nx,ny=0,0,0

queue=deque()
queue.append((nx,ny))
while 1:
    nx=nx+dx[nd]
    ny=ny+dy[nd]
    time+=1
    if nx<0 or n<=nx or ny<0 or n<=ny or (nx,ny) in queue:
        break
    queue.append((nx,ny))
    if board[nx][ny]==0:
        queue.popleft()
    else:
        board[nx][ny]=0
    if time==go_list[i][0]:
        if go_list[i][1]=='D':
            nd=(nd+1)%4
        else:
            nd=(nd+3)%4
        if i+1<len(go_list):
            i+=1

     
print(time)