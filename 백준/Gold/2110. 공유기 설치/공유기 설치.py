import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#공유기

n,c=map(int,input().split())

home=[]
for _ in range(n):
    home.append(int(input()))

home.sort()
start=1 #가장 가까운거리
end=home[-1]-home[0] #가장 먼 거리

result=0

while start<=end:
    h_now=home[0]
    cnt=1
    mid=(end+start)//2
    for i in range(1,n):
        if home[i]-h_now>=mid:
            cnt+=1
            h_now=home[i]
    if cnt>=c: #cnt가 같은 경우에도 인접한 공유기 거리의 최댓값을 구하기 위하여 start 을 바꿔줌
        start=mid+1
        result = mid
    else: 
        end=mid-1


print(result)