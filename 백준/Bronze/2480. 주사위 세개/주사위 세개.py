a,b,c=map(int,input().split())

if a==b and b==c:
    reward=1000*a+10000
elif a==b or a==c:
    reward=100*a+1000
elif b==c:
    reward=100*b+1000
else:
    big=max(a,b,c)
    reward=big*100

print(reward)