import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy

#뒤집기

s=list(map(int,input().strip()))

cnt_0=0
cnt_1=0
#0연속 묶음
for i in range(len(s)):
    if i==0:
        if s[i]==0:
            cnt_0+=1
    elif s[i-1]==1 and s[i]==0:
        cnt_0+=1
    else:
        continue

#1연속 묶음
for i in range(len(s)):
    if i==1:
        if s[i]==1:
            cnt_1+=1
    elif s[i-1]==0 and s[i]==1:
        cnt_1+=1
    else:
        continue

print(min(cnt_0,cnt_1))
    