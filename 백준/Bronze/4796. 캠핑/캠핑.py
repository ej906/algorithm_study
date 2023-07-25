#캠핑

import sys
input=sys.stdin.readline

i=1

while 1 :
    l,p,v=map(int,input().split())
    if p==0 and l==0 and v==0: break #종료조건
    if v%p>l:
        print("Case "+str(i)+":", v//p*l + l)
    else:
        print("Case "+str(i)+":", v//p*l + v%p)
    i+=1