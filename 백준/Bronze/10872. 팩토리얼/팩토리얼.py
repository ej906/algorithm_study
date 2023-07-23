import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy
INF=1e9

#팩토리얼

n=int(input())

def pactorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*pactorial(n-1)
    
print(pactorial(n))