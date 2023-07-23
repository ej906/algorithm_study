import sys
input=sys.stdin.readline

n=int(input())
n=1000-n
cash_list=[500,100,50,10,5,1]
cnt=0

for i in cash_list:
    if n==0:
        break
    if n>=i:
        cnt+=n//i
        n%=i

print(cnt)