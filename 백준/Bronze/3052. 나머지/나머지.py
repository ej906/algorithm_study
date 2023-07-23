import sys
num=[0]*10
remain=[0]*42
for i in range(10):
    n=int(sys.stdin.readline())
    remain[n%42]+=1

count=0
for i in range(0,42):
    if remain[i]!=0:
        count+=1

print(count)
