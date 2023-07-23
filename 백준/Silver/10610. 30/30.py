import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy
INF=1e9

#30

n=int(input())

num_list=list(map(int,str(n)))
num_list.sort(reverse=True)
sum_num=sum(num_list)

if sum_num%3!=0 or 0 not in num_list:
    print(-1)
else:
    for i in num_list:
        print(i,end='')
    print()
