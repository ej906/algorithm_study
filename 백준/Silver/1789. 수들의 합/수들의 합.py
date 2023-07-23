import sys
input=sys.stdin.readline

s=int(input())
i=1
cnt=0
sum=0

while sum<s:
    sum+=i
    i+=1
    cnt+=1

if sum==s:
    print(cnt)
else:
    print(cnt-1)