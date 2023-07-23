import sys
input=sys.stdin.readline

n=int(input())

point=[]
for i in range(n):
    x,y=map(int,input().strip().split())
    point.append([x,y])

point.sort(key=lambda x:x[1])
point.sort(key=lambda x:x[0])

for i in range(n):
    print(point[i][0],point[i][1])