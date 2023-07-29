
import sys
input=sys.stdin.readline

#수리공 항승

n,l=map(int,input().split())

leak=list(map(int,input().split()))
start=1001
end=1001
cnt=0
leak.sort()

for i in leak:
    if start<=i-0.5 and i+0.5<=end:
        continue
    else:
        start=i-0.5
        end=start+l
        cnt+=1

print(cnt)