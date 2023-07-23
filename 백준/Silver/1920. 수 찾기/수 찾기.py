import sys
input=sys.stdin.readline

n=int(input())

a=list(map(int,input().split()))
a.sort()
m=int(input())

find=list(map(int,input().split()))

start=0
end=len(a)-1

def binary_search(array,target,start,end):
    mid=(start+end)//2
    if start>end:
        return 0
    if array[mid]==target:
        return 1
    elif array[mid]>target:
        return binary_search(a,target,start,mid-1)
    else :
        return binary_search(a,target,mid+1,end)

    
for i in find:
    print(binary_search(a,i,start,end))