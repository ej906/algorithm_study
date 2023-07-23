a,b = map(int,input().split())
c=int(input())

b=b+c
if b>59:
    a+=b//60
    b%=60
    if a>23:
        a-=24

print(a,b)