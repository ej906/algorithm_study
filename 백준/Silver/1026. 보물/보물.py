import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().strip().split()))
B=list(map(int,input().strip().split()))

B.sort()
A.sort(reverse=True)
sum=0

for i in range(n):
    sum+=A[i]*B[i]

print(sum)