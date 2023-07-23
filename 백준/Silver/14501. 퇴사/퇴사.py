import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#퇴사

n=int(input())
day=[]
for i in range(n):
    day.append(list(map(int,input().split())))

dp=[0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+day[i][0],n+1):
        if dp[j]<dp[i]+day[i][1]:
            dp[j]=dp[i]+day[i][1]

print(dp[-1])
