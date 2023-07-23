import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import heapq
import copy
INF=1e9

#더하기 사이클

n=int(input())

cnt=1
change_n=n
while 1:
    a=change_n//10 #10의자리
    b=change_n%10  #1의 자리
    r=(a+b)%10 #합한 수 1의자리 
    change_n=10*b+r
    #print(change_n)
    if change_n!=n:
        cnt+=1
    else:
         break


print(cnt)
    