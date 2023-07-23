import sys
input=sys.stdin.readline

n=list(map(int,input().strip()))

sum1=0
for i in range(len(n)//2):
    sum1+=n[i]

sum2=0
for i in range(len(n)//2,len(n)):
    sum2+=n[i]

if sum1==sum2:
    print("LUCKY")
else:
    print("READY")