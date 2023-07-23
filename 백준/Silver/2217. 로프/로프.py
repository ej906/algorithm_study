import sys
input=sys.stdin.readline

n=int(input())
kg=[]
for i in range(n):
    kg.append(int(input().strip()))


kg.sort()
sum=0
for i in range(n):
    if sum < kg[i]*(n-i):
        sum=kg[i]*(n-i)
print(sum)