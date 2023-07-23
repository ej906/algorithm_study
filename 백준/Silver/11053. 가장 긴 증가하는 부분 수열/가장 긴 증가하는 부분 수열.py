import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#가장 긴 증가하는 부분 수열

n=int(input())

a=list(map(int,input().split()))
count=[0]
dp=[1 for _ in range(n)]
for i in range(n):
   for j in range(i):
      if a[j]<a[i]:
         dp[i]=max(dp[i],dp[j]+1)

print(max(dp))