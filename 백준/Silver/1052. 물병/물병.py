
import sys
import heapq
input=sys.stdin.readline

#물병

n,k=map(int,input().split())

cnt=0

while bin(n).count('1')>k: #2진수로 바꾸고 그중 1인것(컵)의 개수를 센다
    n+=1
    cnt+=1

print(cnt)