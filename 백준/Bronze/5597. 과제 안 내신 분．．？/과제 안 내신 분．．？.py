import sys
count=[0]*31

for i in range(28):
    n=int(sys.stdin.readline())
    count[n]+=1

for i in range(1,31):
    if count[i]==0:
        print(i)
