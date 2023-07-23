import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
x=int(input().strip())

arr=[0]*(x+1)

arr[1]=0

for i in range(2,x+1):
    arr[i]=arr[i-1]+1
    if i%2==0:
        arr[i]=min(arr[i//2]+1,arr[i])
    if i%3==0:
        arr[i]=min(arr[i//3]+1,arr[i])

print(arr[x])