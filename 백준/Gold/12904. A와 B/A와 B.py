
import sys
import heapq
input=sys.stdin.readline

#A와 B

s=list(map(str,input().strip()))
t=list(map(str,input().strip()))
make=0
if t==s:
    make=1

while t: #t에 값이 남아있는 동안
    if t[-1]=='A':
        t.pop() #맨 끝문자 삭제
    elif t[-1]=='B':
        t.pop()
        t.reverse()
    if t==s:
        make=1
        break

if make==1:
    print(1)
else:
    print(0)
