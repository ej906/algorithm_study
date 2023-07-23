import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

#국영수

n=int(input())
score=[]
for _ in range(n):
    name,kor,eng,math=map(str,input().split())
    score.append((name,int(kor),int(eng),int(math)))

score.sort(key=lambda x:x[0])
score.sort(key=lambda x:-x[3])
score.sort(key=lambda x:x[2])
score.sort(key=lambda x:-x[1])

for i in range(len(score)):
    print(score[i][0])