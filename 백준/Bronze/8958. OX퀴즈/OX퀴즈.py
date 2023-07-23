import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy
INF=1e9

#ox퀴즈

t=int(input())

for i in range(t):
    result=list(map(str,input().strip()))
    cnt=0
    score=0
    for i in result:
        if i=='O':
            cnt+=1
            score+=cnt
        else:
            cnt=0
    print(score)  