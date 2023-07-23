import sys
input=sys.stdin.readline
alpabet_list=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
num=input().strip()
sum=0

for i in num:
    for j in range(8):
        if i in alpabet_list[j]:
            sum+=j+3
            
print(sum)