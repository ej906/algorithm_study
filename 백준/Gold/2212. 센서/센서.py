
import sys
import heapq
input=sys.stdin.readline

#센서

n=int(input())
k=int(input())

sensor=list(map(int,input().split()))

sensor.sort()

dis=[]

for i in range(1,n):
    dis.append(sensor[i]-sensor[i-1])

dis.sort()

sum=0

for j in range(n-k):
    sum+=dis[j]

print(sum)