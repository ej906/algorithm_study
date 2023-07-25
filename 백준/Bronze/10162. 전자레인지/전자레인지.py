#전자레인지

import sys
input=sys.stdin.readline

t=int(input())

def microwave(time):
    if time%10!=0:
        print(-1)
    else:
        print(time//300,end=' ')
        time%=300
        print(time//60,end=' ')
        time%=60
        print(time//10)

microwave(t)