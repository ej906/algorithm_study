import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#안테나

n=int(input())

house=list(map(int,input().split()))
house.sort()

print(house[(n-1)//2])