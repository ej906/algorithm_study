import sys
input=sys.stdin.readline

n=int(input())

time=[]

for i in range(n):
    start,end=map(int,input().split())
    time.append([start,end])

time = sorted(time, key=lambda x : x[0])
time = sorted(time, key=lambda x : x[1])

last_end=0
cnt=0

for x,y in time:
    if x>=last_end:
        cnt+=1
        last_end=y

print(cnt)