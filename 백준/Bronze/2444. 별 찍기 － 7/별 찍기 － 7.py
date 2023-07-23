import sys
input=sys.stdin.readline

n=int(input())
star=[]
for i in range(1,n+1):
    star=' '*(n-i)+'*'*(2*i-1)
    print(star)
  
for i in range(n-1,0,-1):
    star=' '*(n-i)+'*'*(2*i-1)
    print(star)
  