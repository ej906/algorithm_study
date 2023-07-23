import sys
input=sys.stdin.readline

t=int(input())

f_01=[]
f_01.append([1,0])
f_01.append([0,1])
for i in range(2,41):
    f_01.append([f_01[i-1][0]+f_01[i-2][0],f_01[i-1][1]+f_01[i-2][1]])

for _ in range(t):
    n=int(input())
    print(f_01[n][0], f_01[n][1])