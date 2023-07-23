import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#나무 자르기

n,m=map(int,input().split())
tree=list(map(int,input().split()))
tree.sort()
start=0
end=tree[-1]
result=0

while start<=end:
    cut=0
    mid=(start+end)//2
    for i in tree:
        if i>mid:
            cut+=(i-mid)
    if cut>=m:
        result=mid
        start=mid+1
    else :
        end=mid-1

print(result)