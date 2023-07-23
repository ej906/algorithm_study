import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy
INF=1e9

#숫자의 개수

a=int(input())
b=int(input())
c=int(input())

result=a*b*c

num_list=list(map(int,str(result)))
#print(num_list)
num_cnt=[0]*10
for i in range(10):
    num_cnt[i]+=num_list.count(i)

for i in range(10):
    print(num_cnt[i])