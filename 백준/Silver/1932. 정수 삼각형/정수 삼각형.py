import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#정수 삼각형

n=int(input())
tri=[]

for i in range(n):
    tri.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(tri[i])):
        if j==0:
            tri[i][j]+=tri[i-1][0]
        elif j==len(tri[i])-1:
            tri[i][j]+=tri[i-1][j-1]
        else:
            tri[i][j]+=max(tri[i-1][j],tri[i-1][j-1])

print(max(tri[n-1]))
    