import sys
yong=[0]*9
index=0
max=0

for i in range(9):
    yong[i]=int(sys.stdin.readline())
    if yong[i]>max:
        index,max=i,yong[i]

print(max,index+1,sep='\n')
