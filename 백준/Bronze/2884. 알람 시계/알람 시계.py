h,m=map(int,input().split())

m1=m-45
if m1<0:
    m1=60+m1
    h-=1
if h<0:
    h=24+h
print(h,m1)