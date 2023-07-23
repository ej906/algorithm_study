import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy
INF=1e9

#카드 정렬하기

n=int(input())
card=[]

for i in range(n):
    heapq.heappush(card,int(input()))

card.sort()

if n==1:
    print(0)
else:
    result=0
    while len(card)>1:
        first=heapq.heappop(card)
        second=heapq.heappop(card)
        result+=(first+second)
        heapq.heappush(card,first+second)
    print(result)
