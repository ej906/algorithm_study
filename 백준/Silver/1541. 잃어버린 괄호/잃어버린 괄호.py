import sys
input=sys.stdin.readline

line=list(input().strip().split('-'))
num=[0]*len(line)

for i in range(len(line)):
    plus=list(line[i].split('+'))
    for j in plus:
        num[i]+=int(j)

sum=num[0]

for i in range(1,len(num)):
    sum-=num[i]

print(sum)
