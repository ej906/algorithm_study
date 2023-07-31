
import sys
import heapq
input=sys.stdin.readline

#행복유치원

n,k=map(int,input().split())

student=list(map(int,input().split()))
student.sort()

cost=[]
for i in range(1,n):
    cost.append(student[i]-student[i-1])
cost.sort()

sum=0
for i in range(n-k): #(n-1)-(k-1)
    sum+=cost[i]

print(sum)