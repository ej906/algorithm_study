
import sys
import heapq
input=sys.stdin.readline

#신입사원

t=int(input())

for _ in range(t):
    n=int(input())
    score=[]
    for _ in range(n):
        document,interview=map(int,input().split())
        score.append([document,interview])
    
    score.sort()
    accept=1 #document가 0순위인 사람

    min=score[0][1]
    for i in range(1,n):
        if min>score[i][1]:
            accept+=1
            min=score[i][1]
    
    print(accept)
