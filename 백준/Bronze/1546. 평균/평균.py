import sys

n=int(input())

score=[0]*n

score=list(map(int,sys.stdin.readline().split()))

max_score=max(score)
sum=0

for i in range(n):
    score[i]=score[i]/max_score*100
    sum+=score[i]

print(sum/n)